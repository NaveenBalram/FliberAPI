from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean, Integer

from app.db.base_class import Base


class TargetAssets(Base):
    __tablename__ = "TargetAssets"

    Type = Column(String, nullable=False)
    MinAgeLimit = Column(Integer, nullable=False)
    MaxAgeLimit = Column(Integer, nullable=False)
    MinAmount = Column(Integer, nullable=False)
    MaxAmount = Column(Integer, nullable=False)
    Equity = Column(String, nullable=False)
    Debt = Column(String, nullable=False)
    Gold = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
