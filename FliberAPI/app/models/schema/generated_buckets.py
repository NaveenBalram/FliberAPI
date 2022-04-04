from uuid import UUID

from app.models.schema.base import BaseSchema


class GeneratedBucketsSchemaBase(BaseSchema):
    Name: str
    NetNPV: float
    Investment: float
    Growth: float
    UserId = UUID


class GeneratedBucketsSchema(GeneratedBucketsSchemaBase):
    Id: UUID


class InGeneratedBucketsSchema(GeneratedBucketsSchema):
    ...


class OutGeneratedBucketsSchema(GeneratedBucketsSchema):
    ...
