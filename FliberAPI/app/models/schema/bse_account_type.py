from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class BseAccountTypeSchemaBase(BaseSchema):

    Code: int
    Details: str
    CreatedOn: datetime


class BseAccountTypeSchema(BseAccountTypeSchemaBase):
    Id: UUID


class InBseAccountTypeSchema(BseAccountTypeSchemaBase):
    ...


class OutBseAccountTypeSchema(BseAccountTypeSchema):
    ...
