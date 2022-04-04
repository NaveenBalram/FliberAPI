from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class FrequencySchemaBase(BaseSchema):
    Name: str
    Value: int
    Description: str
    AdvisorId: UUID
    Ref_Id: int
    CreatedOn: datetime
    UpdatedOn: datetime


class FrequencySchema(FrequencySchemaBase):
    Id: UUID


class InFrequencySchema(FrequencySchemaBase):
    ...


class OutFrequencySchema(FrequencySchema):
    ...
