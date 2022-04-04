from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class EpfCalculation(Base):
    __tablename__ = "EpfCalculation"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    Type = Column(String, nullable=True)
    Name = Column(String, nullable=True)
    CurrentBalance = Column(Float, nullable=True)
    AmountSavedSoFor = Column(Float, nullable=True)
    YearlyContribution = Column(Float, nullable=True)
    AnnualGrowthRate = Column(Float, nullable=True)
    EquityPercentage = Column(Float, nullable=True)
    ExpectedValueAtRetirement = Column(Float, nullable=True)
    NumberOfYears = Column(Integer, nullable=True)
    ReturnOnInvestment = Column(Float, nullable=True)
    MaturityYear = Column(Integer, nullable=True)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=True)
