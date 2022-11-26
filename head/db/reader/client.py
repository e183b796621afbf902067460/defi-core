from typing import List
from sqlalchemy.engine.row import Row

from head.interfaces.db.clients.interface import IClient
from head.decorators.singleton import singleton


@singleton
class DBReaderClient(IClient):

    def execute(self, query: str, *args, **kwargs) -> List[Row]:
        return self.engine.execute(statement=query).fetchall()
