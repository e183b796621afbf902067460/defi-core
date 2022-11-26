from abc import ABC
from sqlalchemy.engine.base import Engine


class ISettings(ABC):
    DB_ADDRESS = None
    DB_USER = None
    DB_PASSWORD = None
    DB_NAME = None

    DB_URL = None
    DB_ENGINE = None

    def get_engine(self) -> Engine:
        return NotImplemented("Interface doesn't have an Engine")

    def get_uri(self) -> str:
        return NotImplemented("Interface doesn't have an URI")
