from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class MorningStarNavsSchemaBase(BaseSchema):

    AssetTypeId: UUID
    FundName: str
    NavAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class MorningStarNavsSchema(MorningStarNavsSchemaBase):
    Id: UUID


class InMorningStarNavsSchema(MorningStarNavsSchemaBase):
    ...


class OutMorningStarNavsSchema(MorningStarNavsSchema):
    ...
