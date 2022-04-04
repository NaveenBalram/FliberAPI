from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class OthersCalculationSchemaBase(BaseSchema):
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


class OthersCalculationSchema(OthersCalculationSchemaBase):
    Id: UUID


class InOthersCalculationSchema(OthersCalculationSchemaBase):
    ...


class OutOthersCalculationSchema(OthersCalculationSchema):
    ...

    