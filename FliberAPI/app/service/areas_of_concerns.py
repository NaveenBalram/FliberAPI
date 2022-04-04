import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.areas_of_concerns import AreasOfConcernsRepository
from app.models.schema.areas_of_concerns import (
    InAreasOfConcernsSchema,
    AreasOfConcernsSchema,
)

logger = logging.getLogger(__name__)


class AreasOfConcernsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._areas_of_concerns_repository = AreasOfConcernsRepository(self._db_session)

    async def create(
            self, payload: InAreasOfConcernsSchema
    ):
        areas_of_concerns = await self._areas_of_concerns_repository.create(payload)
        return areas_of_concerns

    async def get_by_id(self, uuid: UUID):
        areas_of_concerns = await self._areas_of_concerns_repository.get_by_id(uuid)
        return areas_of_concerns

    async def get_all(self):
        areas_of_concerns = await self._areas_of_concerns_repository.get_all()
        return areas_of_concerns

    async def delete(self, uuid: UUID):
        return await self._areas_of_concerns_repository.delete(uuid)

    async def update(self, payload: AreasOfConcernsSchema):
        await self._areas_of_concerns_repository.update(payload)

    async def delete_areas_of_concerns_by_user_id(self, user_id: UUID):
        return await self._areas_of_concerns_repository.delete_by_user_id(user_id)
