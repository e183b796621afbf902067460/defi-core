from head.interfaces.abstracts.interface import IAbstractFabric
from head.interfaces.fabrics.interface import IConcreteFabric


class BridgeConfigurator:

    def __init__(self, abstractFabric: IAbstractFabric, fabricKey: str, productKey: str) -> None:
        self._abstractFabric: IAbstractFabric = abstractFabric
        self._fabricKey: str = fabricKey
        self._productKey: str = productKey

    @property
    def abstractFabric(self) -> IAbstractFabric:
        return self._abstractFabric

    def produceFabric(self) -> IConcreteFabric:
        return self.abstractFabric.getFabric(self._fabricKey)

    def produceProduct(self):
        return self.produceFabric().getProduct(self._productKey)
