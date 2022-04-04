from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthFixedDepositData(Base):
    __tablename__ = "NetWorthFixedDepositData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    AccountNumber = Column(String, nullable=True)
    MaturityDate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    PrincipalAmount = Column(Float, nullable=True)
    MaturityAmount = Column(Float, nullable=True)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
