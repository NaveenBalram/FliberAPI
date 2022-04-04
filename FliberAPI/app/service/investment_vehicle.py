import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.investment_vehicle import InvestmentVehicleRepository
from app.models.schema.investment_vehicle import (
    InInvestmentVehicleSchema,
    InvestmentVehicleSchema,
)

logger = logging.getLogger(__name__)


class InvestmentVehicleService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._investment_vehicle_repository = InvestmentVehicleRepository(self._db_session)

    async def create(
            self, payload: InInvestmentVehicleSchema
    ):
        investment_vehicle = await self._investment_vehicle_repository.create(payload)

        return investment_vehicle

    async def get_by_id(self, uuid: UUID):
        investment_vehicle = await self._investment_vehicle_repository.get_by_id(uuid)
        return investment_vehicle

    async def get_all(self):
        investment_vehicle = await self._investment_vehicle_repository.get_all()
        return investment_vehicle

    async def delete(self, uuid: UUID):
        await self._investment_vehicle_repository.delete(uuid)

    async def update(self, payload: InvestmentVehicleSchema):
        await self._investment_vehicle_repository.update(payload)

    async def delete_investment_vehicle_by_user_id(self, user_id: UUID):
        await self._investment_vehicle_repository.delete_by_user_id(user_id)
