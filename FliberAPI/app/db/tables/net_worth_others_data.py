from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthOthersData(Base):
    __tablename__ = "NetWorthOthersData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    AssetName = Column(String, nullable=False)
    TodaysValue = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    PlannedForLiquidity = Column(String, nullable=False)
    TargetLiquidityYear = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    ExpectedPrice = Column(String, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
