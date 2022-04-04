from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class EventTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class EventTypeSchema(EventTypeSchemaBase):
    Id: UUID


class InEventTypeSchema(EventTypeSchemaBase):
    ...


class OutEventTypeSchema(EventTypeSchema):
    ...
