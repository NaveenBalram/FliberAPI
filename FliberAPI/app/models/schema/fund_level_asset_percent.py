from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class FundLevelAssetPercentSchemaBase(BaseSchema):

    AssetTypeId: UUID
    FundTypeId: UUID
    FundName: str
    NavPercent: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class FundLevelAssetPercentSchema(FundLevelAssetPercentSchemaBase):
    Id: UUID


class InFundLevelAssetPercentSchema(FundLevelAssetPercentSchemaBase):
    ...


class OutFundLevelAssetPercentSchema(FundLevelAssetPercentSchema):
    ...
