from uuid import UUID

from app.models.schema.base import BaseSchema


class InvestmentTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    Ref_Id: int


class InvestmentTypeSchema(InvestmentTypeSchemaBase):
    Id: UUID


class InInvestmentTypeSchema(InvestmentTypeSchemaBase):
    ...


class OutInvestmentTypeSchema(InvestmentTypeSchema):
    ...
