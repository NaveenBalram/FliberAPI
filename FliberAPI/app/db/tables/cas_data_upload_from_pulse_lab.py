from sqlalchemy import Column, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class CasDataUploadFromPulseLab(Base):
    __tablename__ = "CasDataUploadFromPulseLab"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CasFile = Column(String, nullable=False)
    Password = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
