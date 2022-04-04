from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, text, Integer, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class GoalCategory(Base):
    __tablename__ = "GoalCategory"

    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    GoalTypeId = Column(UUID(as_uuid=True), ForeignKey("GoalType.Id"))
    RateId = Column(UUID(as_uuid=True), ForeignKey("Rate.Id"))
    FrequencyId = Column(UUID(as_uuid=True), ForeignKey("Frequency.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
