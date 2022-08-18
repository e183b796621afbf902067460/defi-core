from abc import ABC, abstractmethod


class IConcreteFabri(ABC):

    def __init__(self) -> None:
        self._products: dict = dict()

    @abstractmethod
    def addProduct(self) -> None:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.addProduct.__name__}() implementation")

    @abstractmethod
    def getProduct(self) -> object:
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getProduct.__name__}() implementation")
