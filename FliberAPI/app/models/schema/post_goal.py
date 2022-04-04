from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PostGoalSchemaBase(BaseSchema):
    Name: str
    Priority: int
    Type: str
    At: int
    To: int
    Frequency: str
    PresentValue: bool
    Amount: int
    GrowthRate: float
    CreatedOn: datetime
    UpdateOn: datetime
    UserId: str


class PostGoalSchema(PostGoalSchemaBase):
    Id: UUID


class InPostGoalSchema(PostGoalSchemaBase):
    ...


class OutPostGoalSchema(PostGoalSchema):
    ...
