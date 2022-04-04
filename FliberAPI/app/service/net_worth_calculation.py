import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_calculation import NetWorthCalculationRepository
from app.models.schema.net_worth_calculation import OutNetWorthCalculationSchema, NetWorthCalculationSchema, InNetWorthCalculationSchema

logger = logging.getLogger(__name__)


class NetWorthCalculationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._net_worth_calculation_repository = NetWorthCalculationRepository(self._db_session)

    async def create(self, payload: InNetWorthCalculationSchema):
        net_worth_calculation = await self._net_worth_calculation_repository.create(payload)

        return net_worth_calculation

    async def get_by_id(self, uuid: UUID):
        net_worth_calculation = await self._net_worth_calculation_repository.get_by_id(uuid)
        return net_worth_calculation

    async def get_all(self):
        net_worth_calculation = await self._net_worth_calculation_repository.get_all()
        return net_worth_calculation

    async def delete(self, uuid: UUID):
        await self._net_worth_calculation_repository.delete(uuid)

    async def update(self, payload: NetWorthCalculationSchema):
        await self._net_worth_calculation_repository.update(payload)

    async def get_data_by_id(self, user_id):
        return await self._net_worth_calculation_repository.get_data_by_id(user_id)

    