from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean

from app.db.base_class import Base


class NetWorthBucketData(Base):
    __tablename__ = "NetWorthBucketData"

    Name = Column(String, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
