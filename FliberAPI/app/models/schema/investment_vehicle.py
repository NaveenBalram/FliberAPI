from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class InvestmentVehicleSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    InvestmentTypeId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class InvestmentVehicleSchema(InvestmentVehicleSchemaBase):
    Id: UUID


class InInvestmentVehicleSchema(InvestmentVehicleSchemaBase):
    ...


class OutInvestmentVehicleSchema(InvestmentVehicleSchema):
    ...
