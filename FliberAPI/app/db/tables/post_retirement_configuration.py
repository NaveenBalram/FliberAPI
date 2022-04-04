from sqlalchemy import Column, Integer, Float, TIMESTAMP, text, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class PostRetirementConfiguration(Base):
    __tablename__ = "PostRetirementConfiguration"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    RetirementAge = Column(Integer, nullable=False)
    LifeExpectancy = Column(Integer, nullable=False)
    CorpusAmount = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
