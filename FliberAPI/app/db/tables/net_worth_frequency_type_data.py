from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean, Integer

from app.db.base_class import Base


class NetWorthFrequencyTypeData(Base):
    __tablename__ = "NetWorthFrequencyTypeData"

    Name = Column(String, nullable=False)
    Months = Column(Integer, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
