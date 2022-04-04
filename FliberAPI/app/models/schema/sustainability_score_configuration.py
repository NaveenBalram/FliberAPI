from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class SustainabilityScoreConfigurationSchemaBase(BaseSchema):
    RetirementAge: int
    Inflation: int
    LifeExp: int
    RateOfReturn: int
    HealthCareInflation: int
    CreatedOn: datetime
    UpdatedOn: datetime


class SustainabilityScoreConfigurationSchema(
    SustainabilityScoreConfigurationSchemaBase
):
    Id: UUID


class InSustainabilityScoreConfigurationSchema(
    SustainabilityScoreConfigurationSchemaBase
):
    ...


class OutSustainabilityScoreConfigurationSchema(SustainabilityScoreConfigurationSchema):
    ...
