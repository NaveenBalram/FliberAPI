from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class ExpenseCategorySchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    ExpenseTypeId: UUID
    ExpenseInflationRate: UUID
    ExpenseFrequency: UUID
    CreatedOn: datetime
    UpdatedOn: datetime
    Ref_Id: int


class ExpenseCategorySchema(ExpenseCategorySchemaBase):
    Id: UUID


class InExpenseCategorySchema(ExpenseCategorySchemaBase):
    ...


class OutExpenseCategorySchema(ExpenseCategorySchema):
    ...
