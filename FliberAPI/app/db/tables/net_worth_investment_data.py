from sqlalchemy import Column, TIMESTAMP, func, text, Boolean, String, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthInvestmentData(Base):
    __tablename__ = "NetWorthInvestmentData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    AccountNumber = Column(String, nullable=False)
    StartDate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    MaturityDate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    PrincipalAmount = Column(Float, nullable=False)
    MaturityAmount = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
