from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PostCashLadderSchemaBase(BaseSchema):
    RetirementAge: int
    LifeExpectancy: int
    UserId: UUID
    CorpusAmount: float
    Constraint: int
    CheckConstraint: bool
