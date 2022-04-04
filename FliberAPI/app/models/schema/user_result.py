from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class UserResultSchemaBase(BaseSchema):
    UserId: UUID
    RiskProfile: str
    CreatedOn: datetime
    UpdatedOn: datetime


class UserResultSchema(UserResultSchemaBase):
    Id: UUID


class InUserResultSchema(UserResultSchemaBase):
    ...


class OutUserResultSchema(UserResultSchema):
    ...
