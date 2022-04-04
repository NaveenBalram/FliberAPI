from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PpfCalculationSchemaBase(BaseSchema):
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


class PpfCalculationSchema(PpfCalculationSchemaBase):
    Id: UUID


class InPpfCalculationSchema(PpfCalculationSchemaBase):
    ...


class OutPpfCalculationSchema(PpfCalculationSchema):
    ...
