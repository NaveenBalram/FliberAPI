from sqlalchemy import Column, Float, TIMESTAMP, func, text, Boolean, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthLoanData(Base):
    __tablename__ = "NetWorthLoanData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    LoanType = Column(UUID(as_uuid=True), ForeignKey("NetWorthLoanTypeData.Id"))
    LenderName = Column(String, nullable=False)
    StartYear = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    EndYear = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    OutStandingAmount = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
