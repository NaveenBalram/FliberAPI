import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.stocks_calculation import StocksCalculationRepository
from app.models.schema.stocks_calculation import StocksCalculationSchema, InStocksCalculationSchema

logger = logging.getLogger(__name__)


class StocksCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._stocks_calculation_repository = StocksCalculationRepository(self._db_session)

    async def create(self, payload: InStocksCalculationSchema):
        stocks_calculation = await self._stocks_calculation_repository.create(payload)

        return stocks_calculation

    async def get_by_id(self, uuid: UUID):
        stocks_calculation = await self._stocks_calculation_repository.get_by_id(uuid)
        return stocks_calculation

    async def get_all(self):
        stocks_calculation = await self._stocks_calculation_repository.get_all()
        return stocks_calculation

    async def delete(self, uuid: UUID):
        await self._stocks_calculation_repository.delete(uuid)

    async def update(self, payload: StocksCalculationSchema):
        await self._stocks_calculation_repository.update(payload)
