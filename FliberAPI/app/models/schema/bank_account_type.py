from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BankAccountTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class BankAccountTypeSchema(BankAccountTypeSchemaBase):
    Id: UUID


class InBankAccountTypeSchema(BankAccountTypeSchemaBase):
    ...


class OutBankAccountTypeSchema(BankAccountTypeSchema):
    ...
