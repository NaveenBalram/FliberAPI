from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean

from app.db.base_class import Base


class NetWorthSchemeTypeData(Base):
    __tablename__ = "NetWorthSchemeTypeData"

    Name = Column(String, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
