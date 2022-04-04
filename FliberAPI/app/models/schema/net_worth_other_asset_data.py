from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthOtherAssetDataSchemaBase(BaseSchema):
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


class NetWorthOtherAssetDataSchema(NetWorthOtherAssetDataSchemaBase):
    Id: UUID


class InNetWorthOtherAssetDataSchema(NetWorthOtherAssetDataSchemaBase):
    ...


class OutNetWorthOtherAssetDataSchema(NetWorthOtherAssetDataSchema):
    ...
