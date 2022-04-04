from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthVehicleDataSchemaBase(BaseSchema):

    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    Description: str
    VehicleTypeId: str
    EstimatedValue: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthVehicleDataSchema(NetWorthVehicleDataSchemaBase):
    Id: UUID


class InNetWorthVehicleDataSchema(NetWorthVehicleDataSchemaBase):
    ...


class OutNetWorthVehicleDataSchema(NetWorthVehicleDataSchema):
    ...

