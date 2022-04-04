from sqlalchemy import Column, TIMESTAMP, func, text, Boolean, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NetWorthCalculation(Base):
    __tablename__ = "NetWorthCalculation"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    NetWorthAmount = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
