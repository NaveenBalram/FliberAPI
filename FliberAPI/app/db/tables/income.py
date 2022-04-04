from sqlalchemy import Column, String, TIMESTAMP, text, Integer, Boolean, Float, func

from app.db.base_class import Base


class Income(Base):
    __tablename__ = "Income"

    Name = Column(String, nullable=False)
    Type = Column(Integer, nullable=False)
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
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
