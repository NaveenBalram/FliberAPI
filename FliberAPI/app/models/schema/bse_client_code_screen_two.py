from uuid import UUID

from app.models.schema.base import BaseSchema


class BseClientCodeScreenTwo(BaseSchema):
    UserId: UUID
    IncomeSource: str
    OccupationCode: int
    IncomeSlab: str


class BseClientCodeScreenThree(BaseSchema):
    AddressType: int
    AddressOne: str
    AddressTwo: str
    CityCode: str
    StateCode: str
    PinCode: str
    UserId: UUID


class BseClientCodeScreenFour(BaseSchema):
    UserId: UUID
    SignatureUrl: str
