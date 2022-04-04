from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class SourceOfWealthSchemaBase(BaseSchema):

    Code: int
    Description: str
    CreatedOn: datetime


class SourceOfWealthSchema(SourceOfWealthSchemaBase):
    Id: UUID


class InSourceOfWealthSchema(SourceOfWealthSchemaBase):
    ...


class OutSourceOfWealthSchema(SourceOfWealthSchema):
    ...
