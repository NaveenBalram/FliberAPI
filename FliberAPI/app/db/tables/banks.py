from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Boolean

from app.db.base_class import Base


class Banks(Base):
    __tablename__ = "Banks"

    Name = Column(String, nullable=False)
    Code = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
