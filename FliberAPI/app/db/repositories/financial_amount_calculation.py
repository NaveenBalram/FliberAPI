from typing import Type

from sqlalchemy import func

from app.db.repositories.base import BaseRepository
from app.db.tables.financial_amount_calculation import FinancialAmountCalculation
from app.models.schema.financial_amount_calculation import FinancialAmountCalculationSchemaBase, \
    FinancialAmountCalculationSchema, InFinancialAmountCalculationSchema


class FinancialAmountCalculationRepository(
    BaseRepository[FinancialAmountCalculationSchemaBase, FinancialAmountCalculationSchema, FinancialAmountCalculation]):
    @property
    def _in_schema(self) -> Type[FinancialAmountCalculationSchemaBase]:
        return InFinancialAmountCalculationSchema

    @property
    def _schema(self) -> Type[FinancialAmountCalculationSchema]:
        return FinancialAmountCalculationSchema

    @property
    def _table(self) -> Type[FinancialAmountCalculation]:
        return FinancialAmountCalculation

    async def get_total(self, user_id):
        return await self._db_session.execute(func.sum(self._table.TotalAmount).where(self._table.UserId == user_id))
