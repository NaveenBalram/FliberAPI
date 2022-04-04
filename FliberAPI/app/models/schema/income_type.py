from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class IncomeTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class IncomeTypeSchema(IncomeTypeSchemaBase):
    Id: UUID


class InIncomeTypeSchema(IncomeTypeSchemaBase):
    ...


class OutIncomeTypeSchema(IncomeTypeSchema):
    ...
