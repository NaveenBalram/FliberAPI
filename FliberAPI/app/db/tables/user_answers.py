from datetime import datetime

from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Boolean

from app.db.base_class import Base


class UserAnswers(Base):
    __tablename__ = "UserAnswers"

    QuestionId = Column(String, nullable=False)
    SubQuestionId = Column(String, nullable=False)
    UserAnswer = Column(Integer, nullable=False)
    UserId = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
