from sqlalchemy import (
    Column,
    String,
    ForeignKey,
    Boolean,
    func,
    TIMESTAMP,
    text,
    Integer,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class User(Base):
    __tablename__ = "User"

    Email = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    Password = Column(String, nullable=True)
    StartDate = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )
    Phone = Column(String, nullable=False)
    IsStaff = Column(Boolean)
    IsActive = Column(Boolean)
    GenderId = Column(UUID(as_uuid=True), ForeignKey("Gender.Id"))
    RoleId = Column(UUID(as_uuid=True), ForeignKey("Role.Id"))
    RetirementStatusId = Column(UUID(as_uuid=True), ForeignKey("RetirementStatus.Id"))
    AdvisorId = Column(UUID(as_uuid=True), ForeignKey("Advisor.Id"))
    MaritalStatusId = Column(UUID(as_uuid=True), ForeignKey("MaritalStatus.Id"))
    IsMobileNumberValidated = Column(Boolean)
    IsEmailValidated = Column(Boolean)
    DateOfBirth = Column(
        TIMESTAMP(timezone=True), nullable=True, server_default=text("now()")
    )
    RetirementAge = Column(Integer, nullable=True, default=60)
    LifeExpectancy = Column(Integer, nullable=True, default=85)
    FatherName = Column(String, nullable=True)
    MotherName = Column(String, nullable=True)
    SpouseName = Column(String, nullable=True)
    SpouseDOB = Column(String, nullable=True)
    SpousePan = Column(String, nullable=True)
    BornCityId = Column(String, nullable=True)
    BornStateId = Column(String, nullable=True)
    Nationality = Column(String, nullable=True)
    SourceOfWealth = Column(String, nullable=True)
    OccupationTypes = Column(String, nullable=True)
    ResidentStatus = Column(String, nullable=True)
    IncomeSlab = Column(String, nullable=True)
    AddressType = Column(String, nullable=True)
    AddressLine1 = Column(String, nullable=True)
    AddressLine2 = Column(String, nullable=True)
    CityId = Column(String, nullable=True)
    StateId = Column(String, nullable=True)
    PinCode = Column(String, nullable=True)
    MPIN = Column(Integer, nullable=True)
    IMEINumber = Column(String, nullable=True)
    ModuleType = Column(Integer, nullable=True)
    Status = Column(Integer, nullable=True)
    LastQuestion = Column(Integer, nullable=True)
    IsInitialPaymentIsDone = Column(Boolean)
    IsPanVerified = Column(Boolean)
    LastLogin = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
