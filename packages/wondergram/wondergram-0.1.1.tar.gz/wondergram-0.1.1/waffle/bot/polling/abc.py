from abc import ABC, abstractmethod
from typing import Any, AsyncIterator, Generator, Optional

from waffle.api.abc import ABCAPI
from waffle.errors import ABCErrorHandler


class ABCPolling(ABC):
    api: "ABCAPI"
    error_handler: "ABCErrorHandler"

    @abstractmethod
    async def listen(self) -> AsyncIterator:
        """
        Receives and yields update objects
        """
        pass
