from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class RrScoreConfigurationSchemaBase(BaseSchema):

    RORforEPFOAndGS: int
    EquityRORforNPSandMLI: int
    DebtORforNPSandMLI: int
    InflationRate: int
    RateOfReturn: int
    LifeExp: int
    RetirementAge: int
    CreatedOn: datetime
    UpdatedOn: datetime


class RrScoreConfigurationSchema(RrScoreConfigurationSchemaBase):
    Id: UUID


class InRrScoreConfigurationSchema(RrScoreConfigurationSchemaBase):
    ...


class OutRrScoreConfigurationSchema(RrScoreConfigurationSchema):
    ...
