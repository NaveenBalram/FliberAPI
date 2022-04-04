from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class BseAccountType(Base):
    __tablename__ = "BseAccountType"

    Code = Column(String, nullable=False)
    Details = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
