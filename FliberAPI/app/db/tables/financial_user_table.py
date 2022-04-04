from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class FinancialUserTable(Base):
    __tablename__ = "FinancialUserTable"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    Type = Column(String, nullable=True)
    Name = Column(String, nullable=True)
    CurrentBalance = Column(Float, default=0, nullable=True)
    AmountSavedSoFor = Column(Float, default=0, nullable=True)
    YearlyContribution = Column(Float, default=0, nullable=True)
    AnnualGrowthRate = Column(Float, default=0, nullable=True)
    EquityPercentage = Column(Float, default=0, nullable=True)
    ExpectedValueAtRetirement = Column(Float, default=0, nullable=True)
    NumberOfYears = Column(Integer, default=0, nullable=False)
    ReturnOnInvestment = Column(Float, default=0, nullable=False)
    MaturityYear = Column(Integer, default=0, nullable=True)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, default=False, nullable=False)
