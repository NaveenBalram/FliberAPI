from datetime import datetime
from typing import Optional
from uuid import UUID

from app.models.schema.base import BaseSchema


class PaymentSchemaBase(BaseSchema):

    UserId: UUID
    cf_payment_id: int
    order_id: str
    entity: str
    payment_currency: str
    payment_amount: float
    payment_time: str
    payment_status: str
    payment_message: str
    bank_reference: str
    auth_id: str


class PaymentSchema(PaymentSchemaBase):
    Id: UUID


class InPaymentSchema(PaymentSchemaBase):
    ...


class OutPaymentSchema(PaymentSchema):
    ...
