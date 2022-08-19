from abc import ABC
from web3 import Web3
from web3.providers.base import BaseProvider


class IContract(ABC):

    _abi: str = None

    def __init__(self) -> None:
        self._address = '0x0000000000000000000000000000000000000000'
        self._provider = None
        self._contract = None

    def create(self):
        self._contract = Web3(provider=self.provider).eth.contract(
            address=Web3.toChecksumAddress(value=self.address), abi=self.abi)
        return self

    @property
    def contract(self):
        return self._contract

    @property
    def abi(self) -> str:
        return self._abi

    def getAddress(self) -> str:
        return self._address

    def setAddress(self, address: str):
        self._address: str = address
        return self

    def getProvider(self) -> BaseProvider:
        return self._provider

    def setProvider(self, provider: BaseProvider):
        self._provider: BaseProvider = provider
        return self

    address = property(
        fget=getAddress,
        fset=setAddress
    )

    provider = property(
        fget=getProvider,
        fset=setProvider
    )
