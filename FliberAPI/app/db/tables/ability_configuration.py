from sqlalchemy import Column, Integer, String, text, func, TIMESTAMP, Boolean

from app.db.base_class import Base


class AbilityConfiguration(Base):
    __tablename__ = "AbilityConfiguration"

    LowerLimit = Column(Integer, nullable=False)
    UpperLimit = Column(Integer, nullable=False)
    Type = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
