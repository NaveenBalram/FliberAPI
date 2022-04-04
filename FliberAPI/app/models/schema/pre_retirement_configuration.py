from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class PreRetirementConfigurationSchemaBase(BaseSchema):

    UserId: UUID
    RetirementAge: int
    Inflation: int
    LifeExp: int
    CalculationLimit: int
    HealthCareInflation: int
    GrowthFfIncomeRate: int
    VacationInflation: int
    DiscountingRate: int
    AsIs: int
    Luxury: int
    Modest: int
    CreatedOn: datetime
    UpdatedOn: datetime


class PreRetirementConfigurationSchema(PreRetirementConfigurationSchemaBase):
    Id: UUID


class InPreRetirementConfigurationSchema(PreRetirementConfigurationSchemaBase):
    ...


class OutPreRetirementConfigurationSchema(PreRetirementConfigurationSchema):
    ...
