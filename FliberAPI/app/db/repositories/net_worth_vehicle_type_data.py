from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.net_worth_vehicle_type_data import NetWorthVehicleTypeData
from app.models.schema.net_worth_vehicle_type_data import NetWorthVehicleTypeDataSchemaBase, \
    NetWorthVehicleTypeDataSchema, InNetWorthVehicleTypeDataSchema


class NetWorthVehicleTypeDataRepository(
    BaseRepository[NetWorthVehicleTypeDataSchemaBase, NetWorthVehicleTypeDataSchema, NetWorthVehicleTypeData]):
    @property
    def _in_schema(self) -> Type[NetWorthVehicleTypeDataSchemaBase]:
        return InNetWorthVehicleTypeDataSchema

    @property
    def _schema(self) -> Type[NetWorthVehicleTypeDataSchema]:
        return NetWorthVehicleTypeDataSchema

    @property
    def _table(self) -> Type[NetWorthVehicleTypeData]:
        return NetWorthVehicleTypeData
