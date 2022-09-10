from abc import abstractmethod

from head.interfaces.contracts.builder import IContract
from head.decorators.buildermethod import buildermethod


class IInstrumentOverview(IContract):

    _trader = None

    @abstractmethod
    def getOverview(self, *args, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getOverview.__name__}() implementation")

    @buildermethod
    def setTrader(self, trader):
        self._trader = trader

    def getTrader(self):
        return self._trader

    trader = property(
        fget=getTrader,
        fset=setTrader
    )
