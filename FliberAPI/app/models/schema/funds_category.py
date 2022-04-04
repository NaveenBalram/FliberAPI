from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class FundsCategorySchemaBase(BaseSchema):
    AssetTypeId: UUID
    FundTypeId: UUID
    Type: str
    MinAmount: int
    MaxAmount: int
    FundName: str
    FundPercent: float
    CreatedOn: datetime
    UpdatedOn: datetime


class FundsCategorySchema(FundsCategorySchemaBase):
    Id: UUID


class InFundsCategorySchema(FundsCategorySchemaBase):
    ...


class OutFundsCategorySchema(FundsCategorySchema):
    ...
