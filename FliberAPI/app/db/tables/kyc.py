from sqlalchemy import Column, String, TIMESTAMP, text, func, Boolean

from app.db.base_class import Base


class Kyc(Base):
    __tablename__ = "Kyc"

    FirstPan = Column(String, nullable=False)
    SecPan = Column(String, nullable=False)
    ThirdPan = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
