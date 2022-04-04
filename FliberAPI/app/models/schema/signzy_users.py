from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class SignzyUsersSchemaBase(BaseSchema):

    UserId: UUID
    Email: str
    Phone: str
    Name: str
    UserName: str
    ResponseId: str
    ChannelId: str
    ChannelUserName: str
    ChannelName: str
    ApplicationUrl: str
    MobileLoginUrl: str
    AutoLoginUrl: str
    MobileAutoLoginUrl: str


class SignzyUsersSchema(SignzyUsersSchemaBase):
    Id: UUID


class InSignzyUsersSchema(SignzyUsersSchemaBase):
    ...


class OutSignzyUsersSchema(SignzyUsersSchema):
    ...
