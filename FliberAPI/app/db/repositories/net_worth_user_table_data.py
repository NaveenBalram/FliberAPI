from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_user_table_data import NetWorthUserTableData
from app.models.schema.net_worth_user_table_data import NetWorthUserTableDataSchemaBase, NetWorthUserTableDataSchema, \
    InNetWorthUserTableDataSchema


class NetWorthUserTableDataRepository(
    BaseRepository[NetWorthUserTableDataSchemaBase, NetWorthUserTableDataSchema, NetWorthUserTableData]):
    @property
    def _in_schema(self) -> Type[NetWorthUserTableDataSchemaBase]:
        return InNetWorthUserTableDataSchema

    @property
    def _schema(self) -> Type[NetWorthUserTableDataSchema]:
        return NetWorthUserTableDataSchema

    @property
    def _table(self) -> Type[NetWorthUserTableData]:
        return NetWorthUserTableData
