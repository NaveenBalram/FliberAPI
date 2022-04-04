from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthRentalIncomeDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    Property: str
    RentalInflation: float
    RentalIncomePerYear: datetime
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthRentalIncomeDataSchema(NetWorthRentalIncomeDataSchemaBase):
    Id: UUID


class InNetWorthRentalIncomeDataSchema(NetWorthRentalIncomeDataSchemaBase):
    ...


class OutNetWorthRentalIncomeDataSchema(NetWorthRentalIncomeDataSchema):
    ...
