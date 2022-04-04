from sqlalchemy import Column, String, Float, Integer, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class RuleAssetAllocation(Base):
    __tablename__ = "RuleAssetAllocation"

    RuleId = Column(UUID(as_uuid=True), ForeignKey("RuleCondition.Id"))
    assetType = Column(String, nullable=False)
    AllocationPercentage = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
