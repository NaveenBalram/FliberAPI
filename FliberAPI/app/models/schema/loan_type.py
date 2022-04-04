from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class LoanTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class LoanTypeSchema(LoanTypeSchemaBase):
    Id: UUID


class InLoanTypeSchema(LoanTypeSchemaBase):
    ...


class OutLoanTypeSchema(LoanTypeSchema):
    ...
