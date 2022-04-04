from uuid import UUID

from app.models.schema.base import BaseSchema


class RefundSchemaBase(BaseSchema):
    user_id: UUID
    order_id: str
    cf_refund_id: str
    refund_id: str
    cf_payment_id: int
    entity: str
    refund_amount: float
    refund_currency: str
    refund_note: str
    refund_status: str
    refund_type: str
    failure_reason: str
    created_at: str
    processed_on: str


class RefundSchema(RefundSchemaBase):
    Id: UUID


class InRefundSchema(RefundSchemaBase):
    ...


class OutRefundSchema(RefundSchema):
    ...


class RefundPayload(BaseSchema):
    UserId: UUID
    RefundAmount: int
    RefundNote: str
    OrderId: str
