from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BseCommunicationModeSchemaBase(BaseSchema):

    Code: int
    Details: str
    CreatedOn: datetime


class BseCommunicationModeSchema(BseCommunicationModeSchemaBase):
    Id: UUID


class InBseCommunicationModeSchema(BseCommunicationModeSchemaBase):
    ...


class OutBseCommunicationModeSchema(BseCommunicationModeSchema):
    ...
