from abc import ABC, abstractmethod
from typing import Optional

from head.decorators.buildermethod import buildermethod


class ITraderComponent(ABC):

    _endpoint: Optional[str] = None
    _parent = None

    @abstractmethod
    def getPrice(self, major: str, vs: str) -> float:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getPrice.__name__}() implementation")

    @buildermethod
    def setParent(self, parent: 'ITraderComponent') -> None:
        self._parent = parent

    def getParent(self) -> 'ITraderComponent':
        return self._parent

    parent = property(
        fget=getParent,
        fset=setParent
    )
