from abc import ABC, abstractmethod
from asyncio import AbstractEventLoop
from typing import NoReturn

from waffle.api import ABCAPI
from waffle.bot.polling import ABCPolling


class ABCFramework(ABC):
    api: ABCAPI
    polling: ABCPolling
    loop: AbstractEventLoop

    @abstractmethod
    async def run_polling(self) -> NoReturn:  # type: ignore
        pass

    @abstractmethod
    def run_forever(self) -> NoReturn:  # type: ignore
        pass
