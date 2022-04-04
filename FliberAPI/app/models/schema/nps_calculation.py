from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class NpsCalculationSchemaBase(BaseSchema):

    UserId: UUID
    NpsType: str
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


class NpsCalculationSchema(NpsCalculationSchemaBase):
    Id: UUID


class InNpsCalculationSchema(NpsCalculationSchemaBase):
    ...


class OutNpsCalculationSchema(NpsCalculationSchema):
    ...

    