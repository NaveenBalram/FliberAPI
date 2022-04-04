from datetime import datetime
from uuid import UUID

from app.models.schema.base import BaseSchema


class PaymentTypeSchemaBase(BaseSchema):
    Name: str
    Description: str
    AdvisorId: UUID
    CreatedOn: datetime
    UpdatedOn: datetime


class PaymentTypeSchema(PaymentTypeSchemaBase):
    Id: UUID


class InPaymentTypeSchema(PaymentTypeSchemaBase):
    ...


class OutPaymentTypeSchema(PaymentTypeSchema):
    ...
