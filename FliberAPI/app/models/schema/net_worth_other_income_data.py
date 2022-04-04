from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthOtherIncomeDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    AssetName: str
    TodaysValue: float
    PlannedForLiquidityFlag: str
    TargetLiquidityYear: datetime
    ExpectedPrice: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthOtherIncomeDataSchema(NetWorthOtherIncomeDataSchemaBase):
    Id: UUID


class InNetWorthOtherIncomeDataSchema(NetWorthOtherIncomeDataSchemaBase):
    ...


class OutNetWorthOtherIncomeDataSchema(NetWorthOtherIncomeDataSchema):
    ...

