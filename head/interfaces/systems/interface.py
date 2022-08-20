from abc import ABC, abstractmethod
from typing import Optional


class IPriceSystem(ABC):
    _endpoint: Optional[str] = None
    _instances = dict()

    @abstractmethod
    def getPrice(self, major: str, vs: str):
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getPrice.__name__}() implementation")
