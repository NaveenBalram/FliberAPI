import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.gender import GenderRepository
from app.models.schema.gender import InGenderSchema, GenderSchema

logger = logging.getLogger(__name__)


class GenderService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._gender_repository = GenderRepository(self._db_session)

    async def create(self, payload: InGenderSchema):
        gender = await self._gender_repository.create(payload)

        return gender

    async def get_by_id(self, gender_id: UUID):
        gender = await self._gender_repository.get_by_id(gender_id)
        return gender

    async def get_all(self):
        gender = await self._gender_repository.get_all()
        return gender

    async def delete(self, gender_id: UUID):
        await self._gender_repository.delete(gender_id)

    async def update(self, payload: GenderSchema):
        await self._gender_repository.update(payload)

    async def delete_gender_by_user_id(self, user_id: UUID):
        await self._gender_repository.delete_by_user_id(user_id)
