import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.morning_star_navs import MorningStarNavsRepository
from app.models.schema.morning_star_navs import (
    MorningStarNavsSchema,
    InMorningStarNavsSchema,
)

logger = logging.getLogger(__name__)


class MorningStarNavsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._morning_star_navs_repository = MorningStarNavsRepository(self._db_session)

    async def create(
            self, payload: InMorningStarNavsSchema
    ):
        morning_star_navs = await self._morning_star_navs_repository.create(payload)

        return morning_star_navs

    async def get_by_id(self, uuid: UUID):
        morning_star_navs = await self._morning_star_navs_repository.get_by_id(uuid)
        return morning_star_navs

    async def get_all(self):
        morning_star_navs = await self._morning_star_navs_repository.get_all()
        return morning_star_navs

    async def delete(self, uuid: UUID):
        await self._morning_star_navs_repository.delete(uuid)

    async def update(self, payload: MorningStarNavsSchema):
        await self._morning_star_navs_repository.update(payload)
