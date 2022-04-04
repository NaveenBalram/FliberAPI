from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PortfolioMorningStarSchemaBase(BaseSchema):
    Name: str
    Description: str
    CurrentValue: float
    Reviews: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class PortfolioMorningStarSchema(PortfolioMorningStarSchemaBase):
    Id: UUID


class InPortfolioMorningStarSchema(PortfolioMorningStarSchemaBase):
    ...


class OutPortfolioMorningStarSchema(PortfolioMorningStarSchema):
    ...
