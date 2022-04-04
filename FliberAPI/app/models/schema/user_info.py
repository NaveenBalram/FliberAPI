from uuid import UUID

from app.models.schema.base import BaseSchema


class UserInfoSchemaBase(BaseSchema):
    UserId: UUID
    Text: str


class UserInfoSchema(UserInfoSchemaBase):
    Id: UUID


class InUserInfoSchema(UserInfoSchemaBase):
    ...


class OutUserInfoSchema(UserInfoSchema):
    ...
