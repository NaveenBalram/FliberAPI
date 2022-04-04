from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthStocksDataSchemaBase(BaseSchema):

    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    AssetName: str
    TodaysValue: float
    PlannedForLiquidityFlag: bool
    TargetLiquidityYear: datetime
    ExpectedPrice: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthStocksDataSchema(NetWorthStocksDataSchemaBase):
    Id: UUID


class InNetWorthStocksDataSchema(NetWorthStocksDataSchemaBase):
    ...


class OutNetWorthStocksDataSchema(NetWorthStocksDataSchema):
    ...

