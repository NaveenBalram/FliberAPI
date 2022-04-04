from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    TIMESTAMP,
    text,
    func,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class GeneratedIncomes(Base):
    __tablename__ = "GeneratedIncomes"

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
