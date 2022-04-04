from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthHouseDataSchemaBase(BaseSchema):

    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    Description: str
    PropertyLocation: str
    SOPLOP: str
    RegistrationYear: datetime
    TodaysValue: float
    PlannedForLiquidityFlag: bool
    TargetLiquidityYear: datetime
    ExpectedPrice: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthHouseDataSchema(NetWorthHouseDataSchemaBase):
    Id: UUID


class InNetWorthHouseDataSchema(NetWorthHouseDataSchemaBase):
    ...


class OutNetWorthHouseDataSchema(NetWorthHouseDataSchema):
    ...

