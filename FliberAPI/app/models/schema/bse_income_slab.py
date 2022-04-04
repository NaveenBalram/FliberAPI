from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class BSEIncomeSlabSchemaBase(BaseSchema):

    Code: int
    Description: str
    CreatedOn: datetime


class BSEIncomeSlabSchema(BSEIncomeSlabSchemaBase):
    Id: UUID


class InBSEIncomeSlabSchema(BSEIncomeSlabSchemaBase):
    ...


class OutBSEIncomeSlabSchema(BSEIncomeSlabSchema):
    ...
