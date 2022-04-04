from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Choice(Base):
    __tablename__ = "Choice"

    Text = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    Value = Column(Integer, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    QuestionId = Column(UUID(as_uuid=True), ForeignKey("Question.Id"))
    ChoiceSequence = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
