from sqlalchemy import Column, String, TIMESTAMP, text, Boolean

from app.db.base_class import Base


class NomineeRelation(Base):
    __tablename__ = "NomineeRelation"

    Code = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
