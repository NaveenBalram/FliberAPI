from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Integer,
    TIMESTAMP,
    func,
    text,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class Gender(Base):
    __tablename__ = "Gender"

    Name = Column(String, nullable=False, unique=True)
    Description = Column(String, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
