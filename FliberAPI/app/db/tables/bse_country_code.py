from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean

from app.db.base_class import Base


class BseCountryCode(Base):
    __tablename__ = "BseCountryCode"

    Code = Column(String, nullable=False)
    CountryName = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
