from sqlalchemy import Column, String, TIMESTAMP, text, Integer, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Rate(Base):
    __tablename__ = "Rate"

    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    Code = Column(Integer, nullable=False)
    Percentage = Column(Integer, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    Ref_Id = Column(Integer, default=0)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
