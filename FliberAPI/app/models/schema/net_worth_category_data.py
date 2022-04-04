from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthCategoryDataSchemaBase(BaseSchema):
    Name: str
    BucketId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthCategoryDataSchema(NetWorthCategoryDataSchemaBase):
    Id: UUID


class InNetWorthCategoryDataSchema(NetWorthCategoryDataSchemaBase):
    ...


class OutNetWorthCategoryDataSchema(NetWorthCategoryDataSchema):
    ...
