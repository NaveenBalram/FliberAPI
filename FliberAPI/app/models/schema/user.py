from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.models.schema.base import BaseSchema


class UserSchemaBase(BaseSchema):
    Email: str
    FirstName: str
    LastName: str
    Password: str
    StartDate: datetime
    Phone: str
    ResidentStatus: str
    IsStaff: bool
    IsActive: bool
    GenderId: UUID
    RoleId: UUID
    RetirementStatusId: UUID
    AdvisorId: UUID
    MaritalStatusId: UUID
    IsMobileNumberValidated: bool
    IsEmailValidated: bool
    DateOfBirth: datetime
    MPIN: int
    IMEINumber: str
    CreatedOn: datetime
    UpdatedOn: datetime


class UserSchema(UserSchemaBase):
    Id: UUID


class InUserSchema(UserSchemaBase):
    ...


class OutUserSchema(UserSchemaBase):
    ...


class BseRelatedData(BaseModel):
    UserId: UUID
    FatherName: str
    MotherName: str
    SpouseName: str
    SpouseDOB: str
    SpousePan: str
    BornCityId: str
    BornStateId: str
    Nationality: str
    SourceOfWealth: str
    OccupationTypes: str
    ResidentStatus: str
    IncomeSlab: str
    AddressType: str
    AddressLine1: str
    AddressLine2: str
    CityId: str
    StateId: str
    PinCode: str


class LogoutStatus(BaseModel):
    ModuleType: int
    Status: int
    LastQuestion: int
    LastLogin: datetime
    UserId: UUID


class PhoneDataOutSchema(BaseModel):
    Id: UUID
    Email: str
    FirstName: str
    LastName: str
    StartDate: datetime
    Phone: str
    IsActive: bool
    Gender: str
    RetirementStatus: str
    ResidentStatus: str
    IsMobileNumberValidated: bool
    IsEmailValidated: bool
    DateOfBirth: datetime
    LifeExpectancy: int
    RetirementAge: int
    LastLogin: datetime
    ModuleType: int
    MartialStatus: str
    IsInitialPaymentIsDone: bool
    IsPanVerified: bool
    IMEINumber: str


class UserRegisterSchema(BaseModel):
    Email: str
    FirstName: str
    LastName: str
    Phone: str
    ResidentStatus: str
    DateOfBirth: datetime


class UserStatusSchema(BaseModel):
    UserId: UUID
    GenderId: UUID
    RetirementStatusId: UUID
    MartialStatusId: UUID


class UserPhoneSchema(BaseModel):
    PhoneNumber: Optional[str]
    EmailId: Optional[str]
