from uuid import UUID
from datetime import datetime

from app.models.schema.base import BaseSchema


class BseClientCodeSchemaBase(BaseSchema):

    ClientCode: str
    MemberCode: str
    UserId: UUID
    RegnType: str
    PrimaryHolderFirstName: str
    PrimaryHolderMiddleName: str
    PrimaryHolderLastName: str
    TaxStatus: str
    Gender: str
    PrimaryHolderDobIncorporation: str
    OccupationCode: int
    HoldingNature: str
    SecondHolderFirstName: str
    SecondHolderMiddleName: str
    SecondHolderLastName: str
    ThirdHolderFirstName: str
    ThirdHolderMiddleName: str
    ThirdHolderLastName: str
    SecondHolderDOB: datetime
    ThirdHolderDOB: datetime
    GuardianFirstName: str
    GuardianMiddleName: str
    GuardianLastName: str
    GuardianDOB: datetime
    PrimaryHolderPANExempt: str
    SecondHolderPANExempt: str
    ThirdHolderPANExempt: str
    GuardianPANExempt: str
    PrimaryHolderPAN: str
    SecondHolderPAN: str
    ThirdHolderPAN: str
    GuardianPAN: str
    PrimaryHolderExemptCategory: str
    SecondHolderExemptCategory: str
    ThirdHolderExemptCategory: str
    GuardianExemptCategory: str
    ClientType: str
    PMS: str
    DefaultDP: str
    CDSL_DPID: str
    CDSLCLTID: str
    CMBP_Id: int
    NSDLDPID: str
    NSDLCLTID: str
    # AccountTypeOne: str
    # AccountNoOne: str
    # MICRNoOne: str
    # IFSCCodeOne: str
    # DefaultBankFlagOne: str
    # AccountTypeTwo: str
    # AccountNoTwo: str
    # MICRNoTwo: str
    # IFSCCodeTwo: str
    # DefaultBankFlagTwo: str
    # AccountTypeThree: str
    # AccountNoThree: str
    # MICRNoThree: str
    # IFSCCodeThree: str
    # DefaultBankFlagThree: str
    # AccountTypeFour: str
    # AccountNoFour: str
    # MICRNoFour: str
    # IFSCCodeFour: str
    # DefaultBankFlagFour: str
    # AccountTypeFive: str
    # AccountNoFive: str
    # MICRNoFive: str
    # IFSCCodeFive: str
    # DefaultBankFlagFive: str
    ChequeName: str
    DivPayMode: str
    AddressOne: str
    AddressTwo: str
    AddressThree: str
    City: str
    State: str
    PinCode: str
    Country: str
    ResidentialPhone: str
    ResidentialFax: str
    OfficePhone: str
    OfficeFax: str
    Email: str
    CommunicationMode: str
    ForeignAddressOne: str
    ForeignAddressTwo: str
    ForeignAddressThree: str
    ForeignAddressCity: str
    ForeignAddressPinCode: str
    ForeignAddressState: str
    ForeignAddressCountry: str
    ForeignAddressResidentialPhone: str
    ForeignAddressFax: str
    ForeignAddressOfficePhone: str
    ForeignAddressOfficeFax: str
    IndianMobileNo: str
    # NomineeOneName: str
    # NomineeOneRelationship: str
    # NomineeOneApplicablePercent: float
    # NomineeOneMinorFlag: str
    # NomineeOneDOB: datetime
    # NomineeOneGuardian: str
    # NomineeTwoName: str
    # NomineeTwoRelationship: str
    # NomineeTwoApplicablePercent: str
    # NomineeTwoDOB: datetime
    # NomineeTwoMinorFlag: str
    # NomineeTwoGuardian: str
    # NomineeThreeName: str
    # NomineeThreeRelationship: str
    # NomineeThreeApplicablePercent: float
    # NomineeThreeDOB: datetime
    # NomineeThreeMinorFlag: str
    # NomineeThreeGuardian: str
    PrimaryHolderKYCType: str
    PrimaryHolderCKYCNumber: int
    SecondHolderKYCType: str
    SecondHolderCKYCNumber: int
    ThirdHolderKYCType: str
    ThirdHolderCKYCNumber: int
    GuardianKYCType: str
    GuardianCKYCNumber: int
    PrimaryHolderKRAExemptRefNo: str
    SecondHolderKRAExemptRefNo: str
    ThirdHolderKRAExemptRefNo: str
    GuardianKRAExemptRefNo: str
    AadhaarUpdated: str
    MapInId: str
    PaperLessFlag: str
    LEINo: str
    LEIValidity: datetime
    FillerOne: str
    FillerTwo: str
    FillerThree: str
    SignatureUrl: str
    ChequeUrl: str
    PanCardUrl: str
    CreatedOn: datetime
    UpdatedOn: datetime


class BseClientCodeSchema(BseClientCodeSchemaBase):
    Id: UUID


class InBseClientCodeSchema(BseClientCodeSchemaBase):
    ...


class OutBseClientCodeSchema(BseClientCodeSchema):
    ...
