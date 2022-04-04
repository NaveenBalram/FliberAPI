import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_frequency_type_data import NetWorthFrequencyTypeDataRepository
from app.models.schema.net_worth_frequency_type_data import NetWorthFrequencyTypeDataSchema, \
    InNetWorthFrequencyTypeDataSchema

logger = logging.getLogger(__name__)


class NetWorthFrequencyTypeDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._net_worth_frequency_type_data_repository = NetWorthFrequencyTypeDataRepository(self._db_session)

    async def create(self, payload: InNetWorthFrequencyTypeDataSchema):
        net_worth_frequency_type_data = await self._net_worth_frequency_type_data_repository.create(payload)

        return net_worth_frequency_type_data

    async def get_by_id(self, uuid: UUID):
        net_worth_frequency_type_data = await self._net_worth_frequency_type_data_repository.get_by_id(uuid)
        return net_worth_frequency_type_data

    async def get_all(self):
        net_worth_frequency_type_data = await self._net_worth_frequency_type_data_repository.get_all()
        return net_worth_frequency_type_data

    async def delete(self, uuid: UUID):
        await self._net_worth_frequency_type_data_repository.delete(uuid)

    async def update(self, payload: NetWorthFrequencyTypeDataSchema):
        await self._net_worth_frequency_type_data_repository.update(payload)
