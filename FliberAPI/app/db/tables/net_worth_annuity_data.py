from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthAnnuityData(Base):
    __tablename__ = "NetWorthAnnuityData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CategoryId = Column(UUID(as_uuid=True), ForeignKey("NetWorthCategoryData.Id"))
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    SchemeName = Column(String, nullable=False)
    AccountNumber = Column(String, nullable=False)
    StartDate = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    SchemeType = Column(UUID(as_uuid=True), ForeignKey("NetWorthSchemeTypeData.Id"))
    Corpus = Column(Float, nullable=False)
    AnnuityIncome = Column(Float, nullable=False)
    Frequency = Column(UUID(as_uuid=True), ForeignKey("NetWorthFrequencyTypeData.Id"))
    GrowthOfPension = Column(Float, nullable=False)
    AnnuityMaturity = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)