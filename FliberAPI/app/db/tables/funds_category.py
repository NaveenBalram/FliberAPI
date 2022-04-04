from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, Integer, func, text, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class FundsCategory(Base):
    __tablename__ = "FundsCategory"

    AssetTypeId = Column(UUID(as_uuid=True), ForeignKey("AssetType.Id"))
    FundTypeId = Column(UUID(as_uuid=True), ForeignKey("FundsType.Id"))
    Type = Column(String, nullable=False)
    MinAmount = Column(Integer, nullable=False)
    MaxAmount = Column(Integer, nullable=False)
    FundName = Column(String, nullable=False)
    FundPercent = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
