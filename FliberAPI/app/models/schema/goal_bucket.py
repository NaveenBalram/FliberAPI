from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class GoalBucketSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class GoalBucketSchema(GoalBucketSchemaBase):
    Id: UUID


class InGoalBucketSchema(GoalBucketSchemaBase):
    ...


class OutGoalBucketSchema(GoalBucketSchema):
    ...
