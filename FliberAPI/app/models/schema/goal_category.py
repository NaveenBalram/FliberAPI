from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class GoalCategorySchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    GoalTypeId: UUID
    GoalInflationRate: UUID
    GoalFrequency: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class GoalCategorySchema(GoalCategorySchemaBase):
    Id: UUID


class InGoalCategorySchema(GoalCategorySchemaBase):
    ...


class OutGoalCategorySchema(GoalCategorySchema):
    ...
