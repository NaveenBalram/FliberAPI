from sqlalchemy import Column, String, Float, Integer, TIMESTAMP, func, text, Boolean, Date

from app.db.base_class import Base


class UniverseTable(Base):
    __tablename__ = "UniverseTable"

    mstarid = Column(String, nullable=False)
    ratingdate = Column(Date, nullable=False)
    ratingoveraall = Column(Integer, nullable=False)
    legalname = Column(String, nullable=False)
    fundame = Column(String, nullable=False)
    fundlevelcategoryname = Column(String, nullable=False)
    sharperatio = Column(Float, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
