from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthRentalIncomeData(Base):
    __tablename__ = "NetWorthRentalIncomeData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    Property = Column(String, nullable=False)
    RentalInflation = Column(Float, nullable=False)
    RentalIncomePerYear = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
