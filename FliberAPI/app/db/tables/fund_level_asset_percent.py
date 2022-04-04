from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class FundLevelAssetPercent(Base):
    __tablename__ = "FundLevelAssetPercent"

    AssetTypeId = Column(UUID(as_uuid=True), ForeignKey("AssetType.Id"))
    FundName = Column(String, nullable=False)
    NavPercent = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, nullable=False)
