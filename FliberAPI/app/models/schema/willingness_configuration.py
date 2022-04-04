from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class WillingnessConfigurationSchemaBase(BaseSchema):

    LowerLimit: int
    UpperLimit: int
    Type: str
    CreatedOn: datetime
    UpdatedOn: datetime


class WillingnessConfigurationSchema(WillingnessConfigurationSchemaBase):
    Id: UUID


class InWillingnessConfigurationSchema(WillingnessConfigurationSchemaBase):
    ...


class OutWillingnessConfigurationSchema(WillingnessConfigurationSchema):
    ...
