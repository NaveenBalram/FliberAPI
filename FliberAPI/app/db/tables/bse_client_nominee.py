from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, func, text, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class BseClientNominee(Base):
    __tablename__ = "BseClientNominee"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    NomineeNumber = Column(Integer, nullable=False)
    NomineeName = Column(String, nullable=False)
    NomineeRelationship = Column(String, nullable=False)
    NomineeApplicablePercent = Column(Float, nullable=False)
    NomineeMinorFlag = Column(Boolean, default=False, nullable=False)
    NomineeDOB = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    NomineeGuardian = Column(String, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
