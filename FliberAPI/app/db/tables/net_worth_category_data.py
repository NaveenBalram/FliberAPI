from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class NetWorthCategoryData(Base):
    __tablename__ = "NetWorthCategoryData"

    Name = Column(String, nullable=False)
    BucketId = Column(UUID(as_uuid=True), ForeignKey("NetWorthBucketData.Id"))
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
