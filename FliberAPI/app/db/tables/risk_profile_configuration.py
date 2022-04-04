from sqlalchemy import Column, String, TIMESTAMP, text, func, Boolean

from app.db.base_class import Base


class RiskProfileConfiguration(Base):
    __tablename__ = "RiskProfileConfiguration"

    Type = Column(String, nullable=False)
    Conservative = Column(String, nullable=False)
    ModConservative = Column(String, nullable=False)
    Balanced = Column(String, nullable=False)
    ModAggressive = Column(String, nullable=False)
    Aggressive = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
