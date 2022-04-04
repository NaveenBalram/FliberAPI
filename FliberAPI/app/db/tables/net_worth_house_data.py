from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthHouseData(Base):
    __tablename__ = "NetWorthHouseData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    Description = Column(String, nullable=False)
    PropertyLocation = Column(String, nullable=False)
    SOPLOP = Column(String, nullable=False)
    RegistrationYear = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    TodaysValue = Column(Float, nullable=False)
    PlannedForLiquidity = Column(String, nullable=False)
    TargetLiquidityYear = Column(String, nullable=False)
    ExpectedPrice = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
