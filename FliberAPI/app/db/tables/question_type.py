from datetime import datetime


from sqlalchemy import Column, String, TIMESTAMP, text, Integer, func, Boolean
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class QuestionType(Base):
    __tablename__ = "QuestionType"

    Name = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    AdvisorId = Column(ForeignKey("Advisor.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    Ref_Id = Column(Integer, default=0)
    IsDeleted = Column(Boolean, default=False)
