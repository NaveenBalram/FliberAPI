from sqlalchemy import Column, String, TIMESTAMP, func, text, Boolean

from app.db.base_class import Base


class BseClientTaxStatus(Base):
    __tablename__ = "BseClientTaxStatus"

    Code = Column(String, nullable=False)
    TaxStatus = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
