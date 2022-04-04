from sqlalchemy import Column, String, TIMESTAMP, text, Boolean

from app.db.base_class import Base


class OccupationTypes(Base):
    __tablename__ = "OccupationTypes"

    Code = Column(String, nullable=False)
    Description = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
