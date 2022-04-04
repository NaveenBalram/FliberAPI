import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.frequency import FrequencyRepository
from app.models.schema.frequency import (
    InFrequencySchema,
    FrequencySchema,
)

logger = logging.getLogger(__name__)


class FrequencyService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._frequency_repository = FrequencyRepository(self._db_session)

    async def create(self, payload: InFrequencySchema):
        frequency = await self._frequency_repository.create(payload)

        return frequency

    async def get_by_id(self, uuid: UUID):
        frequency = await self._frequency_repository.get_by_id(uuid)
        return frequency

    async def get_all(self):
        frequency = await self._frequency_repository.get_all()
        return frequency

    async def delete(self, uuid: UUID):
        await self._frequency_repository.delete(uuid)

    async def update(self, payload: FrequencySchema):
        await self._frequency_repository.update(payload)

    async def delete_frequency_by_user_id(self, user_id: UUID):
        await self._frequency_repository.delete_by_user_id(user_id)
