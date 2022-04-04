from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NetWorthLoanDataSchemaBase(BaseSchema):

    UserId: UUID
    CategoryId: UUID
    BucketId: UUID
    LoanType: float
    LenderName: str
    StartYear: datetime
    EndYear: datetime
    OutStandingAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class NetWorthLoanDataSchema(NetWorthLoanDataSchemaBase):
    Id: UUID


class InNetWorthLoanDataSchema(NetWorthLoanDataSchemaBase):
    ...


class OutNetWorthLoanDataSchema(NetWorthLoanDataSchema):
    ...

