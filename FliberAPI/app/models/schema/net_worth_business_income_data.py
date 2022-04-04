from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthBusinessIncomeDataSchemaBase(BaseSchema):
    UserId: str
    CategoryId: UUID
    BucketId: UUID
    Description: str
    YearlyAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthBusinessIncomeDataSchema(NetWorthBusinessIncomeDataSchemaBase):
    Id: UUID


class InNetWorthBusinessIncomeDataSchema(NetWorthBusinessIncomeDataSchemaBase):
    ...


class OutNetWorthBusinessIncomeDataSchema(NetWorthBusinessIncomeDataSchema):
    ...

