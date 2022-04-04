from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BseStateCodeSchemaBase(BaseSchema):

    Code: int
    State: str
    CreatedOn: datetime


class BseStateCodeSchema(BseStateCodeSchemaBase):
    Id: UUID


class InBseStateCodeSchema(BseStateCodeSchemaBase):
    ...


class OutBseStateCodeSchema(BseStateCodeSchema):
    ...
