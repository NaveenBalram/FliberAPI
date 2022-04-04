from uuid import UUID

from app.models.schema.base import BaseSchema


class GeneratedGoalsSchemaBase(BaseSchema):
    UserId: UUID
    Age: int
    GoalName: str
    GoalValue: str
    GoalAtAge: int


class GeneratedGoalsSchema(GeneratedGoalsSchemaBase):
    Id: UUID


class InGeneratedGoalsSchema(GeneratedGoalsSchema):
    ...


class OutGeneratedGoalsSchema(GeneratedGoalsSchema):
    ...
