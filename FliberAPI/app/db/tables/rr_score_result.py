from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class RrScoreResult(Base):
    __tablename__ = "RrScoreResult"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    RRScoreResult = Column(String, nullable=False)
    CorpusRequired = Column(Float, nullable=False)
    ExpectedValueOfExistingInvestments = Column(Float, nullable=False)
    UserAge = Column(Integer, nullable=False)
    RetirementAge = Column(Integer, nullable=True, default=0)
    AmountRequired = Column(Float, nullable=False)
    CreatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text("now()"))
    UpdatedOn = Column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    IsDeleted = Column(Boolean, nullable=False)
