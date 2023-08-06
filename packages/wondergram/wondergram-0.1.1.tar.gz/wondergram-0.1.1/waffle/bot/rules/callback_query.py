from typing import List, Union

from waffle.bot.rules.abc import ABCRule
from waffle.bot.updates import CallbackQueryUpdate


class CallbackData(ABCRule[CallbackQueryUpdate]):
    """
    A rule that checks if callback data is in
    the given list of values.
    """

    def __init__(self, callback_data: Union[str, List[str]]) -> None:
        if isinstance(callback_data, str):
            callback_data = [callback_data]
        self.callback_data = callback_data

    async def check(self, cq: CallbackQueryUpdate) -> bool:
        return cq.data in self.callback_data
