from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class BondsCalculationSchemaBase(BaseSchema):

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


class BondsCalculationSchema(BondsCalculationSchemaBase):
    Id: UUID


class InBondsCalculationSchema(BondsCalculationSchemaBase):
    def __init__(__pydantic_self__, **data: Any):
        super().__init__(data)
        __pydantic_self__.Type = None

    ...


class OutBondsCalculationSchema(BondsCalculationSchema):
    ...

    