from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.schema.base import BaseSchema


class UserGoalsSchemaBase(BaseSchema):
    UserId: UUID
    GoalName: str
    GoalBucketId: UUID
    GoalCategoryId: UUID
    GoalTypeId: UUID
    GoalFrequencyId: UUID
    GoalInflationRate: float
    GoalAmount: float
    GoalAmountType: bool
    EndOfLife: bool
    GoalPriority: int
    GoalStartAge: int
    GoalEndAge: int
    CreatedOn: datetime
    UpdatedOn: datetime


class UserGoalsSchema(UserGoalsSchemaBase):
    Id: UUID


class InUserGoalsSchema(UserGoalsSchema):
    ...


class OutUserGoalsSchema(UserGoalsSchema):
    ...


class GoalsData(BaseModel):
    GoalName: str
    GoalAmount: float
    GoalPriority: int
    GoalInflationRate: float
    GoalStartAge: int
    GoalEndAge: int
    GoalAmountType: bool
    GoalCategoryName: str
    FrequencyName: str
    GoalTypeName: str
