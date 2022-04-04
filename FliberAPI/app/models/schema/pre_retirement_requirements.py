from uuid import UUID

from app.models.schema.base import BaseSchema


class Goal(BaseSchema):
    GoalId: UUID
    Name: str
    Value: str
    AtAge: int


class PreRetirementRequirementSchemaBase(BaseSchema):
    UserId: UUID
    CurrentAge: int
    VacationPlannedFrom: int
    VacationPlannedTill: int
    AvgMonthlyExpense: int
    AvgMonthlyIncome: int
    AvgHealthExpense: int
    VacationCost: int
    CharityPlannedYearly: int
    AdhocIncome: dict
    Goals: list[Goal]


class PreRetirementRequirementSchema(PreRetirementRequirementSchemaBase):
    Id: UUID


class InPreRetirementRequirementSchema(PreRetirementRequirementSchema):
    ...


class OutPreRetirementRequirementSchema(PreRetirementRequirementSchema):
    ...
