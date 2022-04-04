from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class DailyAssetDataSchemaBase(BaseSchema):
    UserId: UUID
    AssetTypeId: UUID
    FundName: str
    NoOfUnits: int
    NavAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime


class DailyAssetDataSchema(DailyAssetDataSchemaBase):
    Id: UUID


class InDailyAssetDataSchema(DailyAssetDataSchemaBase):
    ...


class OutDailyAssetDataSchema(DailyAssetDataSchema):
    ...
