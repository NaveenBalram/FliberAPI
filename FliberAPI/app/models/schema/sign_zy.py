from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

from app.models.schema import base
from app.models.schema.base import BaseSchema


class SignZySchemaBase(BaseSchema):
    UserId: UUID
    SignZyId: str
    Token: str
    TTL: int
    CreatedOn: datetime
    UpdatedOn: datetime


class SignZySchema(SignZySchemaBase):
    Id: UUID


class InSignZySchema(SignZySchemaBase):
    ...


class OutSignZySchema(SignZySchema):
    ...


class SignZyPayload(BaseModel):
    UserId: UUID
    UserName: str
    Name: str
    Email: str
    Phone: str
