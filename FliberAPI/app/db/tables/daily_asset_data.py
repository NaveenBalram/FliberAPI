from sqlalchemy import Column, Integer, String, Float, DateTime, TIMESTAMP, text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class DailyAssetData(Base):
    __tablename__ = "DailyAssetData"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    AssetTypeId = Column(UUID(as_uuid=True), ForeignKey("AssetType.Id"))
    FundName = Column(String, nullable=False)
    NoOfUnits = Column(Integer, nullable=False)
    NavAmount = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
