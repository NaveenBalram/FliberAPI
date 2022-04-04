from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class ExpenseTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class ExpenseTypeSchema(ExpenseTypeSchemaBase):
    Id: UUID


class InExpenseTypeSchema(ExpenseTypeSchemaBase):
    ...


class OutExpenseTypeSchema(ExpenseTypeSchema):
    ...
