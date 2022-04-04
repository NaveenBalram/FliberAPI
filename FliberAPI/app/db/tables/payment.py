from sqlalchemy import Column, String, Float, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Payment(Base):
    __tablename__ = "Payment"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    cf_payment_id = Column(Integer, nullable=False)
    order_id = Column(String, nullable=False)
    entity = Column(String, nullable=False)
    payment_currency = Column(String, nullable=False)
    payment_amount = Column(Float, nullable=False)
    payment_time = Column(String, nullable=False)
    payment_status = Column(String, nullable=False)
    payment_message = Column(String, nullable=False)
    bank_reference = Column(String, nullable=False)
    auth_id = Column(String, nullable=False)
    IsDeleted = Column(Boolean, default=False)
