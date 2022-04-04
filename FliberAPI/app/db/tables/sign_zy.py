from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class SignZy(Base):
    __tablename__ = "SignZy"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    SignZyId = Column(String, nullable=False)
    Token = Column(String, nullable=False)
    TTL = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
