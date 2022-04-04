from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class UsersReBalanceSheetSchemaBase(BaseSchema):

    UserId: UUID
    TargetAssetsId: UUID
    Amount: float
    SIPAccount: bool = False
    SIPAmount: float
    TransactionStatus: str
    ReBalanceStatus: str
    WatchDays: int
    # SIPDay: datetime
    CreatedOn: datetime
    UpdatedOn: datetime


class UsersReBalanceSheetSchema(UsersReBalanceSheetSchemaBase):
    Id: UUID


class InUsersReBalanceSheetSchema(UsersReBalanceSheetSchemaBase):
    ...


class OutUsersReBalanceSheetSchema(UsersReBalanceSheetSchema):
    ...
