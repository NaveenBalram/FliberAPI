from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class EventType(Base):
    __tablename__ = "EventType"

    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
