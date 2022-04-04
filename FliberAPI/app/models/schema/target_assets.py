from datetime import datetime
from uuid import UUID

from pydantic import BaseModel

from app.models.schema.base import BaseSchema


class TargetAssetsSchemaBase(BaseSchema):
    MinAgeLimit: int
    MaxAgeLimit: int
    MinAmount: int
    MaxAmount: int
    Name: str
    Equity: str
    Debt: str
    Gold: str
    CreatedOn: datetime
    UpdatedOn: datetime


class TargetAssetsSchema(TargetAssetsSchemaBase):
    Id: UUID


class InTargetAssetsSchema(TargetAssetsSchemaBase):
    ...


class OutTargetAssetsSchema(TargetAssetsSchema):
    ...


class RequestTargetAssets(BaseModel):
    RetirementAge: str
    Age: str
