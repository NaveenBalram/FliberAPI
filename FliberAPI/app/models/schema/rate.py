from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class RateSchemaBase(BaseSchema):
    Name: str
    Description: str
    Code: int
    Percentage: int
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class RateSchema(RateSchemaBase):
    Id: UUID


class InRateSchema(RateSchemaBase):
    ...


class OutRateSchema(RateSchema):
    ...
