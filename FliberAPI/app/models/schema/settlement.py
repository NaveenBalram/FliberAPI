from uuid import UUID
from datetime import datetime
from app.models.schema.base import BaseSchema


class SettlementSchemaBase(BaseSchema):

    user_id: UUID
    cf_payment_id: int
    order_id: str
    entity: str
    order_amount: int
    payment_time: datetime
    service_charge: int
    service_tax: float
    settlement_amount: float
    cf_settlement_id: int
    transfer_id: int
    transfer_time: datetime
    transfer_utr: str
    order_currency: str
    settlement_currency: str


class SettlementSchema(SettlementSchemaBase):
    Id: UUID


class InSettlementSchema(SettlementSchemaBase):
    ...


class OutSettlementSchema(SettlementSchema):
    ...
