from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class GoalTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class GoalTypeSchema(GoalTypeSchemaBase):
    Id: UUID


class InGoalTypeSchema(GoalTypeSchemaBase):
    ...


class OutGoalTypeSchema(GoalTypeSchema):
    ...
