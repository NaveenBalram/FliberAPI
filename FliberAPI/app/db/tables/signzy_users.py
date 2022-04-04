from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    TIMESTAMP,
    text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class SignzyUsers(Base):
    __tablename__ = "SignzyUsers"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    Email = Column(String, nullable=False)
    Phone = Column(String, nullable=False)
    Name = Column(String, nullable=False)
    UserName = Column(String, nullable=False)
    ResponseId = Column(String, nullable=False)
    ChannelId = Column(String, nullable=False)
    ChannelUserName = Column(String, nullable=False)
    ChannelName = Column(String, nullable=False)
    ApplicationUrl = Column(String, nullable=False)
    MobileLoginUrl = Column(String, nullable=False)
    AutoLoginUrl = Column(String, nullable=False)
    MobileAutoLoginUrl = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
