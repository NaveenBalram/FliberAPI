from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class StocksCalculationSchemaBase(BaseSchema):
    UserId: UUID
    MutualFundType: str
    CurrentBalance: float
    AmountSavedSoFor: float
    YearlyContribution: float
    AnnualGrowthRate: float
    EquityPercentage: float
    ExpectedValueAtRetirement: float
    NumberOfYears: int
    ReturnOnInvestment: float
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class StocksCalculationSchema(StocksCalculationSchemaBase):
    Id: UUID


class InStocksCalculationSchema(StocksCalculationSchemaBase):
    ...


class OutStocksCalculationSchema(StocksCalculationSchema):
    ...
