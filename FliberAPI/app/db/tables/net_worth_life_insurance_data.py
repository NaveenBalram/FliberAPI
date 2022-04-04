
from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthLifeInsuranceData(Base):
    __tablename__ = "NetWorthLifeInsuranceData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    PolicyProvider = Column(String, nullable=False)
    SchemaName = Column(String, nullable=False)
    PolicyNumber = Column(String, nullable=False)
    PolicyType = Column(String, nullable=False)
    StartDate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    PolicyTerm = Column(String, nullable=False)
    SumAssured = Column(Float, nullable=False)
    MaturityValue = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)

