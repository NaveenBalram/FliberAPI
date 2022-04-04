from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    TIMESTAMP,
    text,
    func,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class SustainabilityScoreConfiguration(Base):
    __tablename__ = "SustainabilityScoreConfiguration"

    RetirementAge = Column(Integer, nullable=False)
    Inflation = Column(Integer, nullable=False)
    LifeExp = Column(Integer, nullable=False)
    RateOfReturn = Column(Integer, nullable=False)
    HealthCareInflation = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
