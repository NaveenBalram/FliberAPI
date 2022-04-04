from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_frequency_type_data import NetWorthFrequencyTypeData
from app.models.schema.net_worth_frequency_type_data import NetWorthFrequencyTypeDataSchemaBase, \
    NetWorthFrequencyTypeDataSchema, InNetWorthFrequencyTypeDataSchema


class NetWorthFrequencyTypeDataRepository(
    BaseRepository[NetWorthFrequencyTypeDataSchemaBase, NetWorthFrequencyTypeDataSchema, NetWorthFrequencyTypeData]):
    @property
    def _in_schema(self) -> Type[NetWorthFrequencyTypeDataSchemaBase]:
        return InNetWorthFrequencyTypeDataSchema

    @property
    def _schema(self) -> Type[NetWorthFrequencyTypeDataSchema]:
        return NetWorthFrequencyTypeDataSchema

    @property
    def _table(self) -> Type[NetWorthFrequencyTypeData]:
        return NetWorthFrequencyTypeData
