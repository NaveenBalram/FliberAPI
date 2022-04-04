from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class BseClientAccountSchemaBase(BaseSchema):

    UserId: UUID
    AccountTypeNumber: int
    AccountType: str
    AccountNo: str
    MICRNo: str
    IFSCCode: str
    DefaultBankFlag: bool
    CreatedOn: datetime


class BseClientAccountSchema(BseClientAccountSchemaBase):
    Id: UUID


class InBseClientAccountSchema(BseClientAccountSchemaBase):
    ...


class OutBseClientAccountSchema(BseClientAccountSchema):
    ...
