from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class BanksSchemaBase(BaseSchema):

    Name: str
    Code: int
    CreatedOn: datetime


class BanksSchema(BanksSchemaBase):
    Id: UUID


class InBanksSchema(BanksSchemaBase):
    ...


class OutBanksSchema(BanksSchema):
    ...
