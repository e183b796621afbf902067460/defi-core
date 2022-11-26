from abc import ABC


class ISettings(ABC):
    DB_ADDRESS = None
    DB_USER = None
    DB_PASSWORD = None
    DB_NAME = None

    DB_URL = None
    DB_ENGINE = None
