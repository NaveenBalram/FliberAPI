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


class DailyNavData(Base):
    __tablename__ = "DailyNavData"

    # FundTypeId = Column(UUID(as_uuid=True), ForeignKey("FundType.Id"))
    FundName = Column(String, nullable=False)
    NavAmount = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, nullable=False)
