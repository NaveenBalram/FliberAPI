from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class NetWorthInvestmentDataSchemaBase(BaseSchema):
    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    AccountNumber: str
    StartDate: datetime
    MaturityDate: datetime
    PrincipalAmount: float
    MaturityAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthInvestmentDataSchema(NetWorthInvestmentDataSchemaBase):
    Id: UUID


class InNetWorthInvestmentDataSchema(NetWorthInvestmentDataSchemaBase):
    ...


class OutNetWorthInvestmentDataSchema(NetWorthInvestmentDataSchema):
    ...
