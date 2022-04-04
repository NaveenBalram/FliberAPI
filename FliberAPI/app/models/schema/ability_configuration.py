from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class AbilityConfigurationSchemaBase(BaseSchema):

    LowerLimit: int
    UpperLimit: int
    Type: str
    CreatedOn: datetime
    UpdatedOn: datetime


class AbilityConfigurationSchema(AbilityConfigurationSchemaBase):
    Id: UUID


class InAbilityConfigurationSchema(AbilityConfigurationSchemaBase):
    ...


class OutAbilityConfigurationSchema(AbilityConfigurationSchema):
    ...
