from uuid import UUID

from app.models.schema.base import BaseSchema


class GeneratedCashLadderPreSchemaBase(BaseSchema):
    Age = int
    ExpenseAtAsIs: float
    ExpenseAtLuxury: float
    ExpenseAtModest: float
    HealthCareExpense: float
    VacationExpense: float
    Charity: float
    Income: float
    AdhocIncome: float
    YearlyIncome: float
    NetExpenseAsIs: float
    NetExpenseLuxury: float
    NetExpenseModest: float
    YearlyExpenseLuxury: float
    YearlyExpenseAsIs: float
    YearlyExpenseModest: float
    UserId = UUID


class GeneratedCashLadderPreSchema(GeneratedCashLadderPreSchemaBase):
    Id: UUID


class InGeneratedCashLadderPreSchema(GeneratedCashLadderPreSchemaBase):
    ...


class OutGeneratedCashLadderPreSchema(GeneratedCashLadderPreSchema):
    ...
