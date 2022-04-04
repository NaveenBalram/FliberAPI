from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class EpfCalculationSchemaBase(BaseSchema):

    UserId: UUID
    CurrentBalance: float
    YearlyContribution: int
    GrowthRate: float
    AmountSavedSoFor: int
    ReturnOnInvestment: float
    RateOfReturn: float
    InvestmentPeriod: int
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool


class EpfCalculationSchema(EpfCalculationSchemaBase):
    Id: UUID


class InEpfCalculationSchema(EpfCalculationSchemaBase):
    ...


class OutEpfCalculationSchema(EpfCalculationSchema):
    ...

    