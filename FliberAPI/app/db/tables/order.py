from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Order(Base):
    __tablename__ = "Order"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    OrderId = Column(String, nullable=False)
    CFOrderId = Column(Integer, nullable=False)
    Entity = Column(String, nullable=False)
    CFPaymentId = Column(Integer)
    PaymentMethod = Column(String)
    OrderAmount = Column(Float)
    OrderStatus = Column(String)
    OrderToken = Column(String, nullable=False)
    OrderNote = Column(String)
    CustomerName = Column(String)
    CustomerEmail = Column(String)
    CustomerId = Column(String)
    CustomerPhone = Column(String)
    SettlementsUrl = Column(String)
    PaymentsUrl = Column(String)
    RefundsUrl = Column(String)
    PaymentLink = Column(String)
    OrderTags = Column(String)
    OrderExpiryTime = Column(String)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
