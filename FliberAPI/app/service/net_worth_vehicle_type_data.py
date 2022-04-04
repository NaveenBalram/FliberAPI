import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_vehicle_type_data import NetWorthVehicleTypeDataRepository
from app.models.schema.net_worth_vehicle_type_data import NetWorthVehicleTypeDataSchema, InNetWorthVehicleTypeDataSchema

logger = logging.getLogger(__name__)


class NetWorthVehicleTypeDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

        self._net_worth_vehicle_type_data_repository = NetWorthVehicleTypeDataRepository(self._db_session)

    async def create(self, payload: InNetWorthVehicleTypeDataSchema):
        net_worth_vehicle_type_data = await self._net_worth_vehicle_type_data_repository.create(payload)

        return net_worth_vehicle_type_data

    async def get_by_id(self, uuid: UUID):
        net_worth_vehicle_type_data = await self._net_worth_vehicle_type_data_repository.get_by_id(uuid)
        return net_worth_vehicle_type_data

    async def get_all(self):
        net_worth_vehicle_type_data = await self._net_worth_vehicle_type_data_repository.get_all()
        return net_worth_vehicle_type_data

    async def delete(self, uuid: UUID):
        await self._net_worth_vehicle_type_data_repository.delete(uuid)

    async def update(self, payload: NetWorthVehicleTypeDataSchema):
        await self._net_worth_vehicle_type_data_repository.update(payload)
