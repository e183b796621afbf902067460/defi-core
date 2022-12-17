from abc import abstractmethod

from head.interfaces.contracts.builder import IContract
from head.decorators.buildermethod import buildermethod


class IArbitrageInstrumentOverview(IContract):
    _FEE = None

    _scan_api_url = None
    _scan_api_key = None
    _block_limit = None

    @abstractmethod
    def getOverview(self, *args, **kwargs):
        raise NotImplementedError(f"{self.__class__.__name__} doesn't have an {self.getOverview.__name__}() implementation")

    @buildermethod
    def setScanApiUrl(self, scan_api_url):
        self._scan_api_url = scan_api_url

    def getScanApiUrl(self):
        return self._scan_api_url

    scan_api_url = property(
        fget=getScanApiUrl,
        fset=setScanApiUrl
    )

    @buildermethod
    def setScanApiKey(self, scan_api_key):
        self._scan_api_key = scan_api_key

    def getScanApiKey(self):
        return self._scan_api_key

    scan_api_key = property(
        fget=getScanApiKey,
        fset=setScanApiKey
    )

    @buildermethod
    def setBlockLimit(self, block_limit):
        self._block_limit = block_limit

    def getBlockLimit(self):
        return self._block_limit

    block_limit = property(
        fget=getBlockLimit,
        fset=setBlockLimit
    )

    @property
    def api_uri(self) -> str:
        return self.scan_api_url + 'api?module=block&action=getblocknobytime&timestamp={timestamp}&closest=before&apikey=' + self.scan_api_key
