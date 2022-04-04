from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class InvestmentProfileSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class InvestmentProfileSchema(InvestmentProfileSchemaBase):
    Id: UUID


class InInvestmentProfileSchema(InvestmentProfileSchemaBase):
    ...


class OutInvestmentProfileSchema(InvestmentProfileSchema):
    ...
