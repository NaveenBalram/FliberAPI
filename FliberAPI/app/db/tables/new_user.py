from sqlalchemy import Column, String, TIMESTAMP, func, text, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class NewUser(Base):
    __tablename__ = "NewUser"

    Email = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    StartDate = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    Phone = Column(Integer, nullable=False)
    IsStaff = Column(Boolean, nullable=False)
    IsActive = Column(Boolean, nullable=False)
    GenderId = Column(UUID(as_uuid=True), ForeignKey("Gender.ref_Id"))
    RoleId = Column(UUID(as_uuid=True), ForeignKey("Role.Ref_Id"))
    RetirementStatusId = Column(
        UUID(as_uuid=True), ForeignKey("RetirementStatus.Ref_Id")
    )
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Ref_Id"))
    MaritalStatusId = Column(UUID(as_uuid=True), ForeignKey("MaritalStatus.Ref_Id"))
    CreateOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsMobileNumberValidated = Column(Boolean, nullable=False)
    IsEmailValidated = Column(Boolean, nullable=False)
    DateOfBirth = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
