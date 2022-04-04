from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class IncomeCategorySchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    IncomeTypeId: UUID
    IncomeInflationRate: UUID
    IncomeFrequency: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class IncomeCategorySchema(IncomeCategorySchemaBase):
    Id: UUID


class InIncomeCategorySchema(IncomeCategorySchemaBase):
    ...


class OutIncomeCategorySchema(IncomeCategorySchema):
    ...
