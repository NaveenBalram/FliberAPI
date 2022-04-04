from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class RiskProfileConfigurationSchemaBase(BaseSchema):

    Type: str
    Conservative: str
    ModConservative: str
    Balanced: str
    ModAggressive: str
    Aggressive: str
    CreatedOn: datetime
    UpdatedOn: datetime


class RiskProfileConfigurationSchema(RiskProfileConfigurationSchemaBase):
    Id: UUID


class InRiskProfileConfigurationSchema(RiskProfileConfigurationSchemaBase):
    ...


class OutRiskProfileConfigurationSchema(RiskProfileConfigurationSchema):
    ...
