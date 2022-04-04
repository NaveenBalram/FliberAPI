from sqlalchemy import Column, String, Integer, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class RuleCondition(Base):
    __tablename__ = "RuleCondition"

    Rulenumber = Column(String, nullable=False)
    RiskCategory = Column(String, nullable=False)
    FundingMinAmount = Column(Integer, nullable=False)
    FundingMaxAmount = Column(Integer, nullable=False)
    TimetoRetirementMin = Column(Integer, nullable=False)
    TimetoRetirementMax = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
