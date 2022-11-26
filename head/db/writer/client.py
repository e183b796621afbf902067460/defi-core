from sqlalchemy.engine.cursor import CursorResult

from head.interfaces.db.clients.interface import IClient
from head.decorators.singleton import singleton


@singleton
class DBWriterClient(IClient):

    def execute(self, query: str, *args, **kwargs) -> CursorResult:
        return self.engine.execute(statement=query)
