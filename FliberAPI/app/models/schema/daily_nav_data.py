from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class DailyNavDataSchemaBase(BaseSchema):
    AssetId: UUID
    FundName: str
    NavAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class DailyNavDataSchema(DailyNavDataSchemaBase):
    Id: UUID


class InDailyNavDataSchema(DailyNavDataSchemaBase):
    ...


class OutDailyNavDataSchema(DailyNavDataSchema):
    ...
