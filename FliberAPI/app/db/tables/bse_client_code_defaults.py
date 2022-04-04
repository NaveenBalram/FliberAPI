from sqlalchemy import Column, TIMESTAMP, func, text, Boolean

from app.db.base_class import Base


class UserGoals(Base):
    __tablename__ = "BseClientCodeDefaults"

    RegnType: str
    TaxStatus: int
    OccupationCode: int
    HoldingNature: str
    DefaultBankFlag: str
    DivPayMode: int
    ClientType: str
    AccountType: str
    PrimaryHolderPANExempt: str
    PrimaryHolderKYCType: str
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
