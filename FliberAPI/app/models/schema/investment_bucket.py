from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class InvestmentBucketSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class InvestmentBucketSchema(InvestmentBucketSchemaBase):
    Id: UUID


class InInvestmentBucketSchema(InvestmentBucketSchemaBase):
    ...


class OutInvestmentBucketSchema(InvestmentBucketSchema):
    ...
