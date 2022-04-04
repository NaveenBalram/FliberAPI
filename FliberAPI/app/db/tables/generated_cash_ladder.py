from datetime import datetime
from sqlalchemy import (
    Column,
    String,
    TIMESTAMP,
    text,
    Integer,
    func,
    Float,
    ForeignKey,
    Boolean,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class GeneratedCashLadder(Base):
    __tablename__ = "GeneratedCashLadder"

    Age = Column(Integer, nullable=False)
    NetCF = Column(Float, nullable=False)
    NormalizedCF = Column(Float, nullable=False)
    OpeningBalance = Column(Float, nullable=False)
    TotalGrowth = Column(Float, nullable=False)
    ClosingBalance = Column(Float, nullable=False)
    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
