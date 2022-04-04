from sqlalchemy import Column, Boolean, String, TIMESTAMP, text, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.schema import ForeignKey

from app.db.base_class import Base


class UsersReBalanceSheet(Base):
    __tablename__ = "UsersReBalanceSheet"

    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    TargetAssetsId = Column(UUID(as_uuid=True), ForeignKey("TargetAssets.Id"))
    Amount = Column(Integer, default=0, nullable=False)
    SIPAccount = Column(Boolean, default=False, nullable=True)
    SIPAmount = Column(Integer, default=0, nullable=False)
    TransactionStatus = Column(String, default="InProgress", nullable=False)
    ReBalanceStatus = Column(String, default="Completed", nullable=False)
    WatchDays = Column(Integer, default=0, nullable=False)
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False, nullable=False)
