from uuid import UUID

from app.models.schema.base import BaseSchema


class GeneratedIncomesSchemaBase(BaseSchema):
    Name: str
    Amount: int
    UserId: UUID


class GeneratedIncomesSchema(GeneratedIncomesSchemaBase):
    Id: UUID


class InGeneratedIncomesSchema(GeneratedIncomesSchema):
    ...


class OutGeneratedIncomesSchema(GeneratedIncomesSchema):
    ...
