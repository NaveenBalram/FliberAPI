from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class FinancialUserTableSchemaBase(BaseSchema):
    UserId: str
    Type: str
    Name: str
    CurrentBalance: float
    AmountSavedSoFor: float
    YearlyContribution: float
    AnnualGrowthRate: float
    EquityPercentage: float
    ExpectedValueAtRetirement: float
    NumberOfYears: int
    ReturnOnInvestment: float
    MaturityYear: int
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class FinancialUserTableSchema(FinancialUserTableSchemaBase):
    Id: UUID


class InFinancialUserTableSchema(FinancialUserTableSchemaBase):
    ...


class OutFinancialUserTableSchema(FinancialUserTableSchema):
    ...
