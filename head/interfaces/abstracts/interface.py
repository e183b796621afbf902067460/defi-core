from abc import ABC, abstractmethod
from head.interfaces.fabrics.interface import IConcreteFabric


class IAbstractFabric(ABC):

    def __init__(self) -> None:
        self._fabrics: dict = dict()

    @abstractmethod
    def addFabric(self, *args, **kwargs) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.addFabric.__name__}() implementation")

    @abstractmethod
    def getFabric(self, *args, **kwargs) -> IConcreteFabric:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getFabric.__name__}() implementation")
