from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class NetWorthOtherIncomeData(Base):
    __tablename__ = "NetWorthOtherIncomeData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    Description = Column(String, nullable=False)
    Frequency = Column(UUID(as_uuid=True), ForeignKey("NetWorthFrequencyTypeData.Id"))
    Duration = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    Amount = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
