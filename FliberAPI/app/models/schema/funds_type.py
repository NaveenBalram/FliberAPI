from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class FundsTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class FundsTypeSchema(FundsTypeSchemaBase):
    Id: UUID


class InFundsTypeSchema(FundsTypeSchemaBase):
    ...


class OutFundsTypeSchema(FundsTypeSchema):
    ...
