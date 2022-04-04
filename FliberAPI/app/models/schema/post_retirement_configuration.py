from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PostRetirementConfigurationSchemaBase(BaseSchema):

    UserId: UUID
    RetirementAge: int
    LifeExpectancy: int
    CorpusAmount: float
    CreatedOn: datetime
    UpdatedOn: datetime


class PostRetirementConfigurationSchema(PostRetirementConfigurationSchemaBase):
    Id: UUID


class InPostRetirementConfigurationSchema(PostRetirementConfigurationSchemaBase):
    ...


class OutPostRetirementConfigurationSchema(PostRetirementConfigurationSchema):
    ...
