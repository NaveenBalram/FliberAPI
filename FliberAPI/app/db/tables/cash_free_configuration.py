from sqlalchemy import (
    Column,
    String,
    TIMESTAMP,
    text,
    func,
    Boolean,
)

from app.db.base_class import Base


class CashFreeConfiguration(Base):
    __tablename__ = "CashFreeConfiguration"

    KeyId = Column(String, nullable=False)
    KeySecret = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
