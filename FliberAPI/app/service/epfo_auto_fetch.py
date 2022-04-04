import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.epfo_auto_fetch import EpfoAutoFetchRepository
from app.models.schema.epfo_auto_fetch import OutEpfoAutoFetchSchema, EpfoAutoFetchSchema, InEpfoAutoFetchSchema

logger = logging.getLogger(__name__)


class EpfoAutoFetchService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._epfo_auto_fetch_repository = EpfoAutoFetchRepository(self._db_session)

    async def create(self, payload: InEpfoAutoFetchSchema):
        epfo_auto_fetch = await self._epfo_auto_fetch_repository.create(payload)

        return epfo_auto_fetch

    async def get_by_id(self, uuid: UUID):
        epfo_auto_fetch = await self._epfo_auto_fetch_repository.get_by_id(uuid)
        return epfo_auto_fetch

    async def get_all(self):
        epfo_auto_fetch = await self._epfo_auto_fetch_repository.get_all()
        return epfo_auto_fetch

    async def delete(self, uuid: UUID):
        await self._epfo_auto_fetch_repository.delete(uuid)

    async def update(self, payload: EpfoAutoFetchSchema):
        await self._epfo_auto_fetch_repository.update(payload)

    