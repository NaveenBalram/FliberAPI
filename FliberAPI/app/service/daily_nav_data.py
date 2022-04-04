import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.daily_nav_data import DailyNavDataRepository
from app.models.schema.daily_nav_data import (
    DailyNavDataSchema,
    InDailyNavDataSchema,
)

logger = logging.getLogger(__name__)


class DailyNavDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._daily_nav_data_repository = DailyNavDataRepository(self._db_session)

    async def create(self, payload: InDailyNavDataSchema):
        daily_nav_data = await self._daily_nav_data_repository.create(payload)

        return daily_nav_data

    async def get_by_id(self, uuid: UUID):
        daily_nav_data = await self._daily_nav_data_repository.get_by_id(uuid)
        return daily_nav_data

    async def get_all(self):
        daily_nav_data = await self._daily_nav_data_repository.get_all()
        return daily_nav_data

    async def delete(self, uuid: UUID):
        await self._daily_nav_data_repository.delete(uuid)

    async def update(self, payload: DailyNavDataSchema):
        await self._daily_nav_data_repository.update(payload)
