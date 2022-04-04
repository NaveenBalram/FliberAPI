from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class PhoneApi(Base):
    __tablename__ = "PhoneApi"

    Phone = Column(String, nullable=False)
    Password = Column(String, nullable=False)
    IsMobileVerified = Column(Boolean, nullable=False)
    IsResidentialInformation = Column(Boolean, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, nullable=False)
