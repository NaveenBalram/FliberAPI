from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthBankDepositDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    AccountNumber: str
    BankName: str
    CurrentBalance: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthBankDepositDataSchema(NetWorthBankDepositDataSchemaBase):
    Id: UUID


class InNetWorthBankDepositDataSchema(NetWorthBankDepositDataSchemaBase):
    ...


class OutNetWorthBankDepositDataSchema(NetWorthBankDepositDataSchema):
    ...
