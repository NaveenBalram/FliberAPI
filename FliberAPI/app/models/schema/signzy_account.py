from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class SignzyAccountSchemaBase(BaseSchema):

    UserName: str
    Password: str


class SignzyAccountSchema(SignzyAccountSchemaBase):
    Id: UUID


class InSignzyAccountSchema(SignzyAccountSchemaBase):
    ...


class OutSignzyAccountSchema(SignzyAccountSchema):
    ...
