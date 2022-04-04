from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Float,
    Boolean,
    TIMESTAMP,
    text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from app.db.base_class import Base


class GeneratedCashLadderPre(Base):
    __tablename__ = "GeneratedCashLadderPre"

    Age = Column(Integer)
    ExpenseAtAsIs: Column(Float)
    ExpenseAtLuxury: Column(Float)
    ExpenseAtModest: Column(Float)
    HealthCareExpense: Column(Float)
    VacationExpense: Column(Float)
    Charity: Column(Float)
    Income: Column(Float)
    AdhocIncome: Column(Float)
    YearlyIncome: Column(Float)
    NetExpenseAsIS: Column(Float)
    NetExpenseLuxury: Column(Float)
    NetExpenseModest: Column(Float)
    YearlyExpenseLuxury: Column(Float)
    YearlyExpenseAsIs: Column(Float)
    YearlyExpenseModest: Column(Float)
    UserId = Column(UUID(as_uuid=True), ForeignKey("User.Id"))
    CreatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    UpdatedOn = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=func.now()
    )
    IsDeleted = Column(Boolean, default=False)
