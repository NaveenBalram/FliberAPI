from uuid import UUID

from pydantic import BaseModel

from app.models.schema.base import BaseSchema


class Goals(BaseModel):
    GoalId: int
    Name: int
    value: int
    AtAge: int


class PreRetirementCorpusCalculationSchemaBase(BaseSchema):
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
    goals = list[Goals]


class PreRetirementCorpusCalculationSchema(PreRetirementCorpusCalculationSchemaBase):
    Id: UUID


class InPreRetirementCorpusCalculationSchema(PreRetirementCorpusCalculationSchemaBase):
    ...


class OutPreRetirementCorpusCalculationSchema(PreRetirementCorpusCalculationSchema):
    ...
