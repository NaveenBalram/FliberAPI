import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.rate import RateRepository
from app.models.schema.rate import InRateSchema, RateSchema

logger = logging.getLogger(__name__)


class RateService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._rate_repository = RateRepository(self._db_session)

    async def create(self, payload: InRateSchema):
        rate = await self._rate_repository.create(payload)

        return rate

    async def get_by_id(self, uuid: UUID):
        rate = await self._rate_repository.get_by_id(uuid)
        return rate

    async def get_all(self):
        rate = await self._rate_repository.get_all()
        return rate

    async def delete(self, uuid: UUID):
        await self._rate_repository.delete(uuid)

    async def update(self, payload: RateSchema):
        await self._rate_repository.update(payload)

    async def delete_rate_by_user_id(self, user_id: UUID):
        await self._rate_repository.delete_by_user_id(user_id)
