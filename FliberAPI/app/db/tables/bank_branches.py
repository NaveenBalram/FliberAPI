from sqlalchemy import Column, String, Integer, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class BankBranches(Base):
    __tablename__ = "BankBranches"

    IFSC = Column(String, nullable=False)
    BankId = Column(Integer)
    Branch = Column(String, nullable=False)
    Address = Column(String, nullable=False)
    City = Column(String, nullable=False)
    District = Column(String, nullable=False)
    State = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
