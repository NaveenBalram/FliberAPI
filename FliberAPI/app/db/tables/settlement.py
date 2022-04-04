from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Settlement(Base):
    __tablename__ = "Settlement"

    user_id = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    cf_payment_id = Column(Integer, nullable=False)
    order_id = Column(String, nullable=False)
    entity = Column(String, nullable=False)
    order_amount = Column(Integer, nullable=False)
    payment_time = Column(DateTime, nullable=False)
    service_charge = Column(Integer, nullable=False)
    service_tax = Column(Float, nullable=False)
    settlement_amount = Column(Float, nullable=False)
    cf_settlement_id = Column(Integer, nullable=False)
    transfer_id = Column(Integer, nullable=False)
    transfer_time = Column(DateTime, nullable=False)
    transfer_utr = Column(String, nullable=False)
    order_currency = Column(String, nullable=False)
    settlement_currency = Column(String, nullable=False)
    IsDeleted = Column(Boolean, default=False)
