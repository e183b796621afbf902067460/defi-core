from abc import abstractmethod
from abc import ABC

from head.decorators.buildermethod import buildermethod

from sqlalchemy.engine.base import Engine


class IClient(ABC):

    @abstractmethod
    def execute(self, *args, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.execute.__name__}() implementation")

    @buildermethod
    def setEngine(self, engine: Engine):
        self._engine: Engine = engine

    def getEngine(self) -> Engine:
        return self._engine

    engine = property(
        fget=getEngine,
        fset=setEngine
    )
