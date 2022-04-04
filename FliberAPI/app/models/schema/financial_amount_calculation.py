from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class FinancialAmountCalculationSchemaBase(BaseSchema):
    UserId: str
    Type: str
    Name: str
    TotalAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class FinancialAmountCalculationSchema(FinancialAmountCalculationSchemaBase):
    Id: UUID


class InFinancialAmountCalculationSchema(FinancialAmountCalculationSchemaBase):
    ...


class OutFinancialAmountCalculationSchema(FinancialAmountCalculationSchema):
    ...

    