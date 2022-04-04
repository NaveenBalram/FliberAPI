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


class PreRetirementConfiguration(Base):
    __tablename__ = "PreRetirementConfiguration"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    RetirementAge = Column(Integer, nullable=False)
    Inflation = Column(Integer, nullable=False)
    LifeExp = Column(Integer, nullable=False)
    CalculationLimit = Column(Integer, nullable=False)
    HealthCareInflation = Column(Integer, nullable=False)
    GrowthFfIncomeRate = Column(Integer, nullable=False)
    VacationInflation = Column(Integer, nullable=False)
    DiscountingRate = Column(Integer, nullable=False)
    AsIs = Column(Integer, nullable=False)
    Luxury = Column(Integer, nullable=False)
    Modest = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
