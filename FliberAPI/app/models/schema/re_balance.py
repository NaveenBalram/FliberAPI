from uuid import UUID
from datetime import datetime

from pydantic import BaseModel

from app.models.schema.base import BaseSchema


class ReBalanceSchemaBase(BaseSchema):

    UserId: UUID
    Amount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class ReBalanceSchema(ReBalanceSchemaBase):
    Id: UUID


class InReBalanceSchema(ReBalanceSchemaBase):
    ...


class OutReBalanceSchema(ReBalanceSchema):
    ...


class SIPReBalance(BaseModel):
    UserId: UUID
    Amount: float
    SIPAmount: float
    SIPAccount: bool = False
    SmartSip: bool = False
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool
