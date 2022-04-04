from datetime import datetime

from sqlalchemy import (
    Column,
    String,
    TIMESTAMP,
    Integer,
    ForeignKey,
    func,
    text,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class GeneratedBuckets(Base):
    __tablename__ = "GeneratedBuckets"

    Name = Column(String, nullable=False, unique=True)
    Amount = Column(Integer, nullable=False)
    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
