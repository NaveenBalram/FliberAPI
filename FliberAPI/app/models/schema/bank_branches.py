from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class BankBranchesSchemaBase(BaseSchema):

    IFSC: str
    BankId: UUID
    Branch: str
    Address: str
    City: str
    District: str
    State: str
    CreatedOn: datetime


class BankBranchesSchema(BankBranchesSchemaBase):
    Id: UUID


class InBankBranchesSchema(BankBranchesSchemaBase):
    ...


class OutBankBranchesSchema(BankBranchesSchema):
    ...
