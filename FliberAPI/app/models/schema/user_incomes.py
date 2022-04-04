from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class UserIncomesSchemaBase(BaseSchema):
    UserId: str
    IncomeCategoryId: str
    IncomeTypeId: str
    IncomeFrequencyId: str
    IncomeInflationRate: float
    IncomeStartAge: int
    IncomeEndAge: int
    IncomeAmount: int
    IncomeAmountType: bool
    CreatedOn: datetime
    UpdatedOn: datetime


class UserIncomesSchema(UserIncomesSchemaBase):
    Id: UUID


class InUserIncomesSchema(UserIncomesSchema):
    ...


class OutUserIncomesSchema(UserIncomesSchema):
    ...
