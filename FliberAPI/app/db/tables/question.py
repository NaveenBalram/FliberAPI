from sqlalchemy import Column, String, TIMESTAMP, text, Integer, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class Question(Base):
    __tablename__ = "Question"

    QuestionTitle = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    PreviousQuestionId = Column(Integer, nullable=False)
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    QuestionTypeId = Column(UUID(as_uuid=True), ForeignKey("QuestionType.Id"))
    QuestionSequence = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
