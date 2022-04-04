from datetime import datetime
from uuid import UUID

from pydantic.main import BaseModel

from app.models.schema.base import BaseSchema


class OrderSchemaBase(BaseSchema):

    UserId: UUID
    OrderId: str
    CFOrderId: int
    Entity: str
    CFPaymentId: int
    PaymentMethod: str
    OrderAmount: float
    OrderStatus: str
    OrderToken: str
    OrderNote: str
    OrderExpiryTime: str
    CustomerName: str
    CustomerEmail: str
    CustomerId: str
    CustomerPhone: str
    SettlementsUrl: str
    PaymentsUrl: str
    RefundsUrl: str
    PaymentLink: str
    OrderTags: str
    CreatedOn: datetime
    UpdatedOn: datetime
    IsDeleted: bool = False


class OrderSchema(OrderSchemaBase):
    Id: UUID


class InOrderSchema(OrderSchemaBase):
    ...


class OutOrderSchema(OrderSchema):
    ...


class RequestOrderSchema(BaseModel):
    UserId: UUID
    OrderAmount: float
    OrderCurrency: str
    CustomerId: str
    CustomerEmail: str
    CustomerName: str
    PhoneNo: str
    OrderNote: str
    ExpiryDate: datetime


class RequestOrderPayment(BaseModel):
    OrderToken: str
    CardNumber: str
    CardHolderName: str
    cardExpiryMonth: str
    CardExpiryYear: str
    CardCVV: str
