from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthFixedDepositDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    AccountNumber: str
    MaturityDate: datetime
    PrincipalAmount: float
    MaturityAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthFixedDepositDataSchema(NetWorthFixedDepositDataSchemaBase):
    Id: UUID


class InNetWorthFixedDepositDataSchema(NetWorthFixedDepositDataSchemaBase):
    ...


class OutNetWorthFixedDepositDataSchema(NetWorthFixedDepositDataSchema):
    ...
