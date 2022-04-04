from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class UserInfo(Base):
    __tablename__ = "UserInfo"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    Text = Column(String, nullable=False)
    IsDeleted = Column(Boolean, default=False)
