import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.occupation_types import OccupationTypesRepository
from app.models.schema.occupation_types import (
    InOccupationTypesSchema,
    OccupationTypesSchema,
)

logger = logging.getLogger(__name__)


class OccupationTypesService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._occupation_types_repository = OccupationTypesRepository(self._db_session)

    async def create(
            self, payload: InOccupationTypesSchema
    ):
        occupation_types = await self._occupation_types_repository.create(payload)

        return occupation_types

    async def get_by_id(self, uuid: UUID):
        occupation_types = await self._occupation_types_repository.get_by_id(uuid)
        return occupation_types

    async def get_all(self):
        occupation_types = await self._occupation_types_repository.get_all()
        return occupation_types

    async def delete(self, uuid: UUID):
        await self._occupation_types_repository.delete(uuid)

    async def update(self, payload: OccupationTypesSchema):
        await self._occupation_types_repository.update(payload)

    async def delete_occupation_types_by_user_id(self, user_id: UUID):
        await self._occupation_types_repository.delete_by_user_id(user_id)
