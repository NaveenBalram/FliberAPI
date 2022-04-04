from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthGoldDataSchemaBase(BaseSchema):

    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    TodaysValue: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthGoldDataSchema(NetWorthGoldDataSchemaBase):
    Id: UUID


class InNetWorthGoldDataSchema(NetWorthGoldDataSchemaBase):
    ...


class OutNetWorthGoldDataSchema(NetWorthGoldDataSchema):
    ...

