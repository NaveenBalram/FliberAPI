from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Refund(Base):
    __tablename__ = "Refund"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    order_id = Column(String, nullable=False)
    cf_refund_id = Column(String, nullable=False)
    refund_id = Column(String, nullable=False)
    cf_payment_id = Column(Integer, nullable=False)
    entity = Column(String, nullable=False)
    refund_amount = Column(Float, nullable=False)
    refund_currency = Column(String, nullable=False)
    refund_note = Column(String, nullable=False)
    refund_status = Column(String, nullable=False)
    refund_type = Column(String, nullable=False)
    failure_reason = Column(String, nullable=False)
    created_at = Column(String, nullable=False)
    processed_on = Column(String, nullable=False)
    IsDeleted = Column(Boolean, default=False)
