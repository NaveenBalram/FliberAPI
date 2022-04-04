from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    TIMESTAMP,
    func,
    text,
    ForeignKey,
    Float,
    Integer,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class UserIncomes(Base):
    __tablename__ = "UserIncomes"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    IncomeCategoryId = Column(UUID(as_uuid=True), ForeignKey("IncomeCategory.Id"))
    IncomeTypeId = Column(UUID(as_uuid=True), ForeignKey("IncomeType.Id"))
    IncomeFrequencyId = Column(UUID(as_uuid=True), ForeignKey("Frequency.Id"))
    IncomeInflationRate = Column(Float)
    IncomeStartAge = Column(Integer)
    IncomeEndAge = Column(Integer)
    IncomeAmount = Column(Float)
    IncomeAmountType = Column(Boolean)  # 0 means pv
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, default=False)
