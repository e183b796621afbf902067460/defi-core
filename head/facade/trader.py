from head.interfaces.systems.interface import IPriceSystem
from head.decorators.yieldmethod import yieldmethod
from head.decorators.singleton import singleton


@singleton
class TraderFacade(IPriceSystem):

    def __init__(self, cefiPriceSystem: IPriceSystem, defiPriceSystem: IPriceSystem) -> None:
        self._cefiPriceSystem: IPriceSystem = cefiPriceSystem
        self._defiPriceSystem: IPriceSystem = defiPriceSystem

    @yieldmethod
    def getPrice(self, major: str, vs: str) -> float:
        for subsystem in self.getSubsystems():
            yield subsystem.getPrice(major=major, vs=vs)

    def getSubsystems(self) -> list:
        return [self._cefiPriceSystem, self._defiPriceSystem]
