from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Boolean,
    TIMESTAMP,
    text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class GeneratedGoals(Base):
    __tablename__ = "GeneratedGoals"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    Age = Column(Integer)
    GoalName = Column(String)
    GoalValue = Column(String)
    GoalAtAge = Column(String)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
