import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.financial_amount_calculation import FinancialAmountCalculationRepository
from app.models.schema.financial_amount_calculation import OutFinancialAmountCalculationSchema, FinancialAmountCalculationSchema, InFinancialAmountCalculationSchema

logger = logging.getLogger(__name__)


class FinancialAmountCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._financial_amount_calculation_repository = FinancialAmountCalculationRepository(self._db_session)

    async def create(self, payload: InFinancialAmountCalculationSchema):
        financial_amount_calculation = await self._financial_amount_calculation_repository.create(payload)

        return financial_amount_calculation

    async def get_by_id(self, uuid: UUID):
        financial_amount_calculation = await self._financial_amount_calculation_repository.get_by_id(uuid)
        return financial_amount_calculation

    async def get_all(self):
        financial_amount_calculation = await self._financial_amount_calculation_repository.get_all()
        return financial_amount_calculation

    async def delete(self, uuid: UUID):
        await self._financial_amount_calculation_repository.delete(uuid)

    async def update(self, payload: FinancialAmountCalculationSchema):
        await self._financial_amount_calculation_repository.update(payload)

    async def get_total(self, user_id):
        return await self._financial_amount_calculation_repository.get_total(user_id)


    