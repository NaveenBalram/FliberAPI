from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    Float,
    TIMESTAMP,
    func,
    text,
    ForeignKey,
    Boolean,
    Integer,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class UserGoals(Base):
    __tablename__ = "UserGoals"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    GoalBucketId = Column(UUID(as_uuid=True), ForeignKey("GoalBucket.Id"))
    GoalCategoryId = Column(UUID(as_uuid=True), ForeignKey("GoalCategory.Id"))
    GoalName = Column(String)
    GoalFrequencyId = Column(UUID(as_uuid=True), ForeignKey("Frequency.Id"))
    GoalInflationRate = Column(Float)
    GoalAmount = Column(Float)
    GoalAmountType = Column(Boolean)  # 0 means pv
    EndOfLife = Column(Boolean)
    GoalTypeId = Column(UUID(as_uuid=True), ForeignKey("GoalType.Id"))
    GoalPriority = Column(Integer)
    GoalStartAge = Column(Integer)
    GoalEndAge = Column(Integer)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
