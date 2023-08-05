import inspect
from enum import Enum
from json import JSONDecodeError
from types import SimpleNamespace
from typing import Any, Awaitable, Callable, cast, Generator, NamedTuple, Optional, Type, TYPE_CHECKING, Union
from urllib.parse import parse_qsl, unquote

from aiohttp import hdrs
from aiohttp.abc import AbstractView
from aiohttp.web_exceptions import HTTPException, HTTPMethodNotAllowed
from aiohttp.web_response import Response, StreamResponse
from pydantic import BaseModel
from pydantic.error_wrappers import get_exc_type, ValidationError
from pydantic.errors import BoolError, BytesError, DictError, FloatError, IntegerError, PydanticTypeError, StrError
from pydantic.main import ModelMetaclass

from . import exceptions

if TYPE_CHECKING:
    from pydantic.error_wrappers import ErrorDict


class _ExtractedData(NamedTuple):
    method_params: dict[str, Any]
    validation_errors: dict[str, list['ErrorDict']]


class _ExtractedAnnotations(SimpleNamespace):
    headers: Optional[Type[BaseModel]] = None
    match_info: Optional[Type[BaseModel]] = None
    query_params: Optional[Type[BaseModel]] = None
    body: Optional[Type[BaseModel]] = None
    response: Optional[StreamResponse] = None


class _ResponseSchema(BaseModel):
    errors: Optional[dict[str, list['ErrorDict']]]
    result: Optional[BaseModel] = None

    def set_client_error(self, error: dict[str, list['ErrorDict']]) -> None:
        if self.errors is None:
            self.errors = {}
        self.errors = self.errors | error

    def set_result(self, result: BaseModel) -> None:
        self.result = result


class _HandlerResponseEnumType(str, Enum):
    pydantic_model = 'pydantic_model'
    web_response = 'web_response'
    another = 'another'

    def is_pydantic_model(self) -> bool:
        return self == self.pydantic_model

    def is_web_response(self) -> bool:
        return self == self.web_response

    def is_another(self) -> bool:
        return self == self.another


_MethodResponseType = Union[
    StreamResponse,
    BaseModel,
    tuple[BaseModel, int],
    tuple[BaseModel, HTTPException],
]
_MethodType = Callable[[], Awaitable[_MethodResponseType]]


class _HandlerExpectedAttributes(str, Enum):
    headers = 'headers'
    query_params = 'query_params'
    match_info = 'match_info'
    body = 'body'
    response = 'response'


# TODO дефолтные миддлвари
# TODO создать метод response_schema
# TODO если пользователю нужна своя кастомная схема, он укажет просто свою
# TODO создать абстрактную схему с определенными методами
# TODO простые ответы не учтены (только с http кодом)
# TODO поддержку валидации cookie & form_data
# TODO придумать и написать парсер для файлов - нужно ли в первой итерации?


class FastView(AbstractView):

    _default_response_success_http_code = 200

    def __await__(self) -> Generator[Any, None, StreamResponse]:
        return self._handle_incoming_request().__await__()

    async def _handle_incoming_request(self) -> StreamResponse:
        if self.request.method not in hdrs.METH_ALL:
            self._raise_allowed_methods()

        self._method = self._get_handler_method()

        handler_response_schema = _ResponseSchema()
        response = None

        extract_annotations = self._extract_annotations()

        if extract_annotations.response:
            # TODO проверку по всем основным типам (3)
            if extract_annotations.response is Response:  # TODO is subclass
                # TODO создвать extract_annotations
                response = Response()
            else:
                raise exceptions.WrongAnnotatedWebResponseError(
                    attr_name=_HandlerExpectedAttributes.response,
                    exp_response_type=Response,
                )

        method_params, validate_errors = await self._extract_data(extract_annotations)
        if response is not None:
            method_params[_HandlerExpectedAttributes.response] = response

        if validate_errors:
            handler_response_schema.set_client_error(validate_errors)
            return self._return_json_response(response=Response(), schema=handler_response_schema, status=400)

        method_response = await self._method(**method_params)

        return await self._handle_response(
            handler_response_schema=handler_response_schema,
            method_response=method_response,
            annotated_response=response,
        )

    async def _handle_response(
            self,
            method_response: _MethodResponseType,
            handler_response_schema: _ResponseSchema,
            annotated_response: Optional[StreamResponse],
    ):  # TODO type
        response_http_code = self._default_response_success_http_code

        if isinstance(method_response, tuple):
            try:
                method_response, unchecked_response_http_code = method_response
            except ValueError:
                raise exceptions.HandlerResultTypeError(possible_type=_MethodResponseType)

            response_http_code = self._get_handler_response_http_code(
                existing_response=annotated_response,
                unchecked_http_code=unchecked_response_http_code,
            )

        handler_response_type = self._get_handler_response_type(method_response)

        if handler_response_type.is_pydantic_model():
            handler_response_schema.set_result(cast(BaseModel, method_response))

            if annotated_response is None:
                annotated_response = Response()

            return self._return_json_response(
                response=annotated_response,
                schema=handler_response_schema,
                status=response_http_code,
            )

        if handler_response_type.is_web_response():
            if (annotated_response is not None) and (annotated_response is not method_response):
                raise exceptions.NotOriginalResponseError()

            return method_response

        raise exceptions.UnhandledResponseTypeError(method_response_type=type(method_response))

    def _get_handler_response_type(
            self,
            method_response: Union[BaseModel, StreamResponse, tuple[Any, ...]],
    ) -> _HandlerResponseEnumType:
        if isinstance(method_response, BaseModel):
            return _HandlerResponseEnumType.pydantic_model
        if isinstance(method_response, StreamResponse):
            return _HandlerResponseEnumType.web_response
        return _HandlerResponseEnumType.another

    def _return_json_response(self, response: StreamResponse, schema: _ResponseSchema, status: int):
        response = cast(Response, response)

        try:
            handler_response_schema = schema.json(by_alias=True)
        except Exception as exc:
            raise exceptions.CannotSerializeResponseError(exc=exc)

        response.content_type = 'application/json'
        response.text = handler_response_schema
        if status:
            response.set_status(status)

        return response

    async def _extract_data(self, extract_annotations: _ExtractedAnnotations) -> _ExtractedData:
        method_params = {}
        validation_errors = {}

        if extract_annotations.headers:
            h_result, h_validate_error = self._validate_headers(extract_annotations.headers)
            if h_result:
                method_params[_HandlerExpectedAttributes.headers] = h_result
            else:
                h_validate_error = cast(list['ErrorDict'], h_validate_error)
                validation_errors[_HandlerExpectedAttributes.headers] = h_validate_error

        if extract_annotations.match_info:
            mi_result, mi_validate_error = self._validate_match_info(extract_annotations.match_info)
            if mi_result:
                method_params[_HandlerExpectedAttributes.match_info] = mi_result
            else:
                mi_validate_error = cast(list['ErrorDict'], mi_validate_error)
                validation_errors[_HandlerExpectedAttributes.match_info] = mi_validate_error

        if extract_annotations.query_params:
            qp_result, qp_validate_error = self._validate_query_params(extract_annotations.query_params)
            if qp_result:
                method_params[_HandlerExpectedAttributes.query_params] = qp_result
            else:
                qp_validate_error = cast(list['ErrorDict'], qp_validate_error)
                validation_errors[_HandlerExpectedAttributes.query_params] = qp_validate_error

        if extract_annotations.body:
            body_result, body_validate_error = await self._validate_body_data(extract_annotations.body)
            if body_result:
                method_params[_HandlerExpectedAttributes.body] = body_result
            else:
                validation_errors[_HandlerExpectedAttributes.body] = cast(list['ErrorDict'], body_validate_error)

        return _ExtractedData(method_params=method_params, validation_errors=validation_errors)

    def _get_handler_response_http_code(
            self,
            existing_response: Optional[StreamResponse],
            unchecked_http_code: Any,
    ) -> int:
        if existing_response is not None and (existing_response.status != self._default_response_success_http_code):
            return existing_response.status

        if isinstance(unchecked_http_code, int):
            return unchecked_http_code

        try:
            is_web_http_error = issubclass(unchecked_http_code, HTTPException)
        except TypeError:
            raise exceptions.UnexpectedHttpCodeTypeError(possible_type=Union[int, HTTPException])

        if is_web_http_error:
            return unchecked_http_code.status_code

        raise exceptions.UnexpectedHttpCodeTypeError(possible_type=Union[int, HTTPException])

    def _validate_headers(self, headers_type) -> Union[
        tuple[BaseModel, None],
        tuple[None, list['ErrorDict']],
    ]:
        h_result, errors = self._validate_pydantic_schema(schema=headers_type, data=dict(self.request.headers))
        if errors:
            return None, errors
        return cast(BaseModel, h_result), None

    def _validate_match_info(self, match_info_type) -> Union[
        tuple[BaseModel, None],
        tuple[None, list['ErrorDict']],
    ]:
        fetched_match_info_data = self._fetch_match_info_data()
        mi_result, errors = self._validate_pydantic_schema(schema=match_info_type, data=fetched_match_info_data)
        if errors:
            return None, errors
        return cast(BaseModel, mi_result), None

    def _validate_query_params(self, query_params_type) -> Union[
        tuple[BaseModel, None],
        tuple[None, list['ErrorDict']],
    ]:
        fetched_query_params_data = self._fetch_query_params_data()
        qp_result, errors = self._validate_pydantic_schema(schema=query_params_type, data=fetched_query_params_data)
        if errors:
            return None, errors
        return cast(BaseModel, qp_result), None

    async def _validate_body_data(self, body_type) -> Union[
        tuple[Any, None],
        tuple[None, list['ErrorDict']],
    ]:
        try:
            fetched_body_data = await self._fetch_body_data()
        except exceptions.MissingContentTypeError as missing_content_type_exc:
            return None, self._gef_pydantic_like_answer_by_custom_message(
                loc=(_HandlerExpectedAttributes.body,),
                msg=str(missing_content_type_exc),
            )
        except exceptions.UnexpectedContentTypeError as unexpected_content_type_exc:
            return None, self._gef_pydantic_like_answer_by_custom_message(
                loc=(_HandlerExpectedAttributes.body,),
                msg=str(unexpected_content_type_exc),
            )
        except JSONDecodeError:
            return None, self._gef_pydantic_like_answer_by_custom_message(
                loc=(_HandlerExpectedAttributes.body,),
                msg=str('body is not a json'),
            )
        # TODO errror? На текщуий момент поддерживается только Response?
        # TODO добавить проверку что тип который мы ожидаем совпадает с тем что мы принимаем иначе 400
        # TODO првоерка в др местах
        # TODO проверка is Response -> проверка на несколько видов Response
        if isinstance(body_type, ModelMetaclass):  # the model has not yet been created so check against its metaclass
            fetched_body_data = cast(dict[str, Any], fetched_body_data)
            b_result, errors = self._validate_pydantic_schema(schema=body_type, data=fetched_body_data)
            if errors:
                return None, errors
        else:
            try:
                b_result = body_type(fetched_body_data)
            except (ValueError, TypeError):
                error_message = self._gef_pydantic_like_answer_by_class_type_error(
                    loc=(_HandlerExpectedAttributes.body,),
                    type_error_class=body_type,
                )
                return None, error_message

        return b_result, None

    def _validate_pydantic_schema(self, schema: Any, data: dict[str, Any]) -> Union[
        tuple[BaseModel, None],
        tuple[None, list['ErrorDict']],
    ]:
        try:
            result = schema(**data)
        except ValidationError as ve:
            return None, ve.errors()

        return result, None

    def _fetch_match_info_data(self) -> dict:
        return dict(self.request.match_info)

    def _fetch_query_params_data(self) -> dict:
        return dict(self.request.rel_url.query)

    async def _fetch_body_data(self) -> Union[str, dict[str, Any]]:
        # не хватает xml

        if self._request_content_type is None:
            raise exceptions.MissingContentTypeError()

        if self._request_content_type == 'application/json':
            return await self.request.json()

        if self._request_content_type == 'text/plain':
            return await self.request.text()

        if self._request_content_type == 'application/x-www-form-urlencoded':
            request_text = await self.request.text()
            unquotes_text = unquote(request_text)
            return self._parse_qs(unquotes_text)

        raise exceptions.UnexpectedContentTypeError(content_type=self._request_content_type)

    def _parse_qs(self, qs: str):
        parsed_result: dict[str, Any] = {}
        pairs = parse_qsl(qs)

        for name, value in pairs:
            if name in parsed_result:
                fst_arg = parsed_result[name][0]
                parsed_result[name] = [fst_arg, value]
            else:
                parsed_result[name] = value
        return parsed_result

    @property
    def _request_content_type(self) -> Optional[str]:
        return self.request.headers.get(hdrs.CONTENT_TYPE)

    def _extract_annotations(self) -> _ExtractedAnnotations:
        annotations = _ExtractedAnnotations()

        signature = inspect.signature(self._method)

        for param in signature.parameters.values():
            param_name = param.name
            param_annotation = param.annotation
            if param_annotation is inspect.Parameter.empty:
                raise exceptions.UntypedAttrFindError(param_name=param.name)

            if param_name == _HandlerExpectedAttributes.headers:
                annotations.headers = param_annotation
            elif param_name == _HandlerExpectedAttributes.match_info:
                annotations.match_info = param_annotation
            elif param_name == _HandlerExpectedAttributes.query_params:
                annotations.query_params = param_annotation
            elif param_name == _HandlerExpectedAttributes.body:
                annotations.body = param_annotation
            elif param_name == _HandlerExpectedAttributes.response:
                annotations.response = param_annotation

        return annotations

    def _gef_pydantic_like_answer_by_class_type_error(
            self,
            loc: tuple[Union[int, str], ...],
            type_error_class: Optional[Any],
    ) -> list['ErrorDict']:
        exc = self._get_pydantic_error_type(type_error_class)
        d: 'ErrorDict' = {'loc': loc, 'msg': exc.msg_template, 'type': get_exc_type(exc)}  # type: ignore
        return [d]

    def _gef_pydantic_like_answer_by_custom_message(
            self,
            loc: tuple[Union[int, str], ...],
            msg: str,
    ) -> list['ErrorDict']:
        exc = self._get_unknown_pydantic_type_error(err_msg=msg)
        d: 'ErrorDict' = {'loc': loc, 'msg': exc.msg_template, 'type': get_exc_type(exc)}  # type: ignore
        return [d]

    def _get_pydantic_error_type(self, type_error_class: Any) -> Type[PydanticTypeError]:
        pydantic_error_map = {
            int: IntegerError,
            str: StrError,
            float: FloatError,
            dict: DictError,
            bytes: BytesError,
            bool: BoolError,
        }
        return pydantic_error_map.get(
            type_error_class,
            self._get_unknown_pydantic_type_error(err_msg=f'value is not a {type_error_class}'),
        )

    def _get_unknown_pydantic_type_error(self, err_msg: Any) -> Type[PydanticTypeError]:
        return cast(
            Type[PydanticTypeError],
            type('TypeError', (PydanticTypeError,), {'msg_template': err_msg}),
        )

    def _raise_allowed_methods(self) -> None:
        allowed_methods = {m for m in hdrs.METH_ALL if hasattr(self, m.lower())}
        raise HTTPMethodNotAllowed(self.request.method, allowed_methods)

    def _get_handler_method(self) -> _MethodType:
        method: Optional[_MethodType] = getattr(self, self.request.method.lower(), None)
        if method is None:
            self._raise_allowed_methods()

        return cast(_MethodType, method)
