from uuid import UUID

from app.models.schema.base import BaseSchema


class GeneratedCashLadderSchemaBase(BaseSchema):
    Age = int
    NetCF = float
    NormalizedCF: float
    OpeningBalance: float
    TotalGrowth: float
    ClosingBalance: float
    UserId = UUID


class GeneratedCashLadderSchema(GeneratedCashLadderSchemaBase):
    Id: UUID


class InGeneratedCashLadderSchema(GeneratedCashLadderSchema):
    ...


class OutGeneratedCashLadderSchema(GeneratedCashLadderSchema):
    ...
