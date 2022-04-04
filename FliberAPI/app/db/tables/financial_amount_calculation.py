from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class FinancialAmountCalculation(Base):
    __tablename__ = "FinancialAmountCalculation"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    Type = Column(String, nullable=True)
    Name = Column(String, nullable=True)
    TotalAmount = Column(Float, nullable=True)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
