from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_scheme_type_data import NetWorthSchemeTypeData
from app.models.schema.net_worth_scheme_type_data import NetWorthSchemeTypeDataSchemaBase, NetWorthSchemeTypeDataSchema, NetWorthSchemeTypeDataSchema, InNetWorthSchemeTypeDataSchema


class NetWorthSchemeTypeDataRepository(BaseRepository[NetWorthSchemeTypeDataSchemaBase, NetWorthSchemeTypeDataSchema, NetWorthSchemeTypeData]):
    @property
    def _in_schema(self) -> Type[NetWorthSchemeTypeDataSchemaBase]:
        return InNetWorthSchemeTypeDataSchema

    @property
    def _schema(self) -> Type[NetWorthSchemeTypeDataSchema]:
        return NetWorthSchemeTypeDataSchema

    @property
    def _table(self) -> Type[NetWorthSchemeTypeData]:
        return NetWorthSchemeTypeData
