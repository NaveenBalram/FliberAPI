from sqlalchemy import Boolean
from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class BseClientAccount(Base):
    __tablename__ = "BseClientAccount"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    AccountTypeNumber = Column(Integer, nullable=False)
    AccountType = Column(String, nullable=False)
    AccountNo = Column(String, nullable=False)
    MICRNo = Column(String, nullable=False)
    IFSCCode = Column(String, nullable=False)
    DefaultBankFlag = Column(Boolean, default=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    IsDeleted = Column(Boolean, default=False)
