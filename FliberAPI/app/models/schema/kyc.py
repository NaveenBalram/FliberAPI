from uuid import UUID

from app.models.schema.base import BaseSchema


class KycSchemaBase(BaseSchema):
    UserId: UUID
    Text: str


class KycSchema(KycSchemaBase):
    Id: UUID


class InKycSchema(KycSchemaBase):
    ...


class OutKycSchema(KycSchema):
    ...
