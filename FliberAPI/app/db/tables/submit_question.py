from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class SubmitQuestion(Base):
    __tablename__ = "SubmitQuestion"

    QuestionId = Column(UUID(as_uuid=True), ForeignKey("Question.Id"))
    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    ChoiceId = Column(String, nullable=True)
    UserText = Column(String, nullable=True, default=0)
    SelectedValue = Column(Integer, nullable=False)
    ModuleType = Column(Integer, nullable=False)
    ChoiceSequence = Column(Integer, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
