from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class CasDataUploadToPulseLab(Base):
    __tablename__ = "CasDataUploadToPulseLab"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    ClientId = Column(Integer, nullable=False)
    SchemeFolioNo = Column(String, nullable=False)
    SchemeName = Column(String, nullable=False)
    SchemeCode = Column(String, nullable=False)
    UnitBalance = Column(String, nullable=False)
    CurrentValue = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
