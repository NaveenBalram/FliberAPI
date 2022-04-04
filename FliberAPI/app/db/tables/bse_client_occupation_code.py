from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean

from app.db.base_class import Base


class BseClientOccupationCode(Base):
    __tablename__ = "BseClientOccupationCode"

    Code = Column(String, nullable=False)
    Details = Column(String, nullable=False)
    CreateOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
