from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class ExpenseCategory(Base):
    __tablename__ = "ExpenseCategory"

    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    GoalType = Column(UUID(as_uuid=True), ForeignKey("GoalType.Id"))
    Rate = Column(UUID(as_uuid=True), ForeignKey("Rate.Id"))
    Frequency = Column(UUID(as_uuid=True), ForeignKey("Frequency.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
