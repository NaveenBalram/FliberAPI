from uuid import UUID

from app.models.schema.base import BaseSchema


class BucketSchemaBase(BaseSchema):
    Name: str
    Years: int
    Rate: float
    RealRate: float


class BucketSchema(BucketSchemaBase):
    Id: UUID


class InBucketSchema(BucketSchema):
    pass


class OutBucketSchema(BucketSchema):
    ...
