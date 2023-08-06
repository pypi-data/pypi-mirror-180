from typing import Any, NoReturn, Union, TYPE_CHECKING

from waffle.api.response_validator.abc import ABCResponseValidator
from waffle.errors import TelegramAPIError

if TYPE_CHECKING:
    from waffle.api import ABCAPI, API


class TelegramAPIErrorResponseValidator(ABCResponseValidator):
    async def validate(
        self, _, data: dict, response: Any, ctx_api: Union["ABCAPI", "API"]
    ) -> Union[Any, NoReturn]:
        if response.get("ok"):
            return response.get("result")

        code, msg = response.get("error_code"), response.get("description")

        if ctx_api.ignore_errors:
            return None

        raise TelegramAPIError[code](msg, data)
