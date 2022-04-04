from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class IncomeSchemaBase(BaseSchema):
    Name: str
    Type: str
    At: int
    To: int
    Frequency: str
    PresentValue: bool
    Amount: float
    GrowthRate: float
    CreatedAt: datetime
    UpdatedAt: datetime
    UserId: str


class IncomeSchema(IncomeSchemaBase):
    Id: UUID


class InIncomeSchema(IncomeSchemaBase):
    ...


class OutIncomeSchema(IncomeSchema):
    ...
