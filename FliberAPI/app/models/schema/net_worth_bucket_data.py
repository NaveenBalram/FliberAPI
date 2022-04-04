from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthBucketDataSchemaBase(BaseSchema):
    Name: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthBucketDataSchema(NetWorthBucketDataSchemaBase):
    Id: UUID


class InNetWorthBucketDataSchema(NetWorthBucketDataSchemaBase):
    ...


class OutNetWorthBucketDataSchema(NetWorthBucketDataSchema):
    ...
