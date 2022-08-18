from abc import ABC, abstractmethod


class IConcreteFabric(ABC):

    def __init__(self) -> None:
        self._products: dict = dict()

    @abstractmethod
    def addProduct(self, *args, **kwargs) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.addProduct.__name__}() implementation")

    @abstractmethod
    def getProduct(self, *args, **kwargs) -> object:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have a {self.getProduct.__name__}() implementation")
