from sqlalchemy import Column, Integer, String, Float, Boolean

from app.db.base_class import Base


class Bucket(Base):
    __tablename__ = "Bucket"

    Name = Column(String, nullable=False)
    Years = Column(Integer, default=0)
    Rate = Column(Float, nullable=False)
    RealRate = Column(Float, nullable=False)
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
