from interfaces.abstracts.interface import IAbstractFabric
from interfaces.fabrics.interface import IConcreteFabric


class BridgeConfigurator:

    def __init__(self, abstractFabric: IAbstractFabric, fabricKey: str, productKey: str, *args, **kwargs) -> None:
        self._abstractFabric: IAbstractFabric = abstractFabric
        self._fabricKey: str = fabricKey
        self._productKey: str = productKey
        self._args: tuple = args
        self._kwargs: dict = kwargs

    @property
    def abstractFabric(self) -> IAbstractFabric:
        return self._abstractFabric

    @property
    def fabricKey(self) -> str:
        return self._fabricKey

    @property
    def productKey(self) -> str:
        return self._productKey

    @property
    def args(self) -> tuple:
        return self._args

    @property
    def kwargs(self) -> dict:
        return self._kwargs

    def produceFabric(self) -> IConcreteFabric:
        return self.abstractFabric.getFabric(self.fabricKey)

    def produceProduct(self) -> object:
        return self.produceFabric().getProduct(self.productKey)
