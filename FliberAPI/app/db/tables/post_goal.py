from sqlalchemy import Column, String, TIMESTAMP, text, Integer, Boolean, Float, func

from app.db.base_class import Base


class PostGoal(Base):
    __tablename__ = "PostGoal"

    Name = Column(String, nullable=False)
    Priority = Column(Integer, nullable=False)
    Type = Column(String, nullable=False)
    At = Column(Integer, nullable=False)
    To = Column(Integer, nullable=False)
    Frequency = Column(String, nullable=False)
    PresentValue = Column(Boolean, nullable=False)
    Amount = Column(Integer, nullable=False)
    GrowthRate = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    UserId = Column(String, nullable=False)
    IsDeleted = Column(Boolean, default=False)
