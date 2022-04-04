from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthVehicleTypeDataSchemaBase(BaseSchema):
    Name: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthVehicleTypeDataSchema(NetWorthVehicleTypeDataSchemaBase):
    Id: UUID


class InNetWorthVehicleTypeDataSchema(NetWorthVehicleTypeDataSchemaBase):
    ...


class OutNetWorthVehicleTypeDataSchema(NetWorthVehicleTypeDataSchema):
    ...
