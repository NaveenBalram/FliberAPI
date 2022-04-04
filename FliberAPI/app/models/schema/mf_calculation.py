from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class MfCalculationSchemaBase(BaseSchema):

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
    IsDeleted: bool


class MfCalculationSchema(MfCalculationSchemaBase):
    Id: UUID


class InMfCalculationSchema(MfCalculationSchemaBase):
    ...


class OutMfCalculationSchema(MfCalculationSchema):
    ...

    