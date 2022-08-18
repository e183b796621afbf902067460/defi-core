from abc import ABC, abstractmethod


class IAbstractFabric(ABC):

    def __init__(self) -> None:
        self._fabrics: dict = dict()

    @abstractmethod
    def addFabric(self) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.addFabric.__name__}() implementation")

    @abstractmethod
    def getFabric(self) -> object:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getFabric.__name__}() implementation")
