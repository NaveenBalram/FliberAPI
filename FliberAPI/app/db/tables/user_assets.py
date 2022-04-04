from sqlalchemy import Column, Integer, String, TIMESTAMP, text, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class UserAssets(Base):
    __tablename__ = "UserAssets"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    AssetTypeId = Column(UUID(as_uuid=True), ForeignKey("AssetType.Id"))
    FundName = Column(String, nullable=False)
    NoOfUnits = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
