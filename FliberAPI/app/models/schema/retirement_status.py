from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class RetirementStatusSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class RetirementStatusSchema(RetirementStatusSchemaBase):
    Id: UUID


class InRetirementStatusSchema(RetirementStatusSchemaBase):
    ...


class OutRetirementStatusSchema(RetirementStatusSchema):
    ...
