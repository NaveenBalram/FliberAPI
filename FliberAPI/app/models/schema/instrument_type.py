from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class InstrumentTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class InstrumentTypeSchema(InstrumentTypeSchemaBase):
    Id: UUID


class InInstrumentTypeSchema(InstrumentTypeSchemaBase):
    ...


class OutInstrumentTypeSchema(InstrumentTypeSchema):
    ...
