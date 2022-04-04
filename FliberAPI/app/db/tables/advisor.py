from sqlalchemy import Column, Integer, String, text, func, TIMESTAMP, Boolean

from app.db.base_class import Base


class Advisor(Base):
    __tablename__ = "Advisor"

    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
