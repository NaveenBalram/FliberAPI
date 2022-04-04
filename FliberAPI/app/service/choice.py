import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.choice import ChoiceRepository
from app.models.schema.choice import InChoiceSchema, ChoiceSchema

logger = logging.getLogger(__name__)


class ChoiceService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._choice_repository = ChoiceRepository(self._db_session)

    async def create(self, payload: InChoiceSchema):
        choice = await self._choice_repository.create(payload)

        return choice

    async def get_by_id(self, uuid: UUID):
        choice = await self._choice_repository.get_by_id(uuid)
        return choice

    async def get_all(self):
        choice = await self._choice_repository.get_all()
        return choice

    async def delete(self, uuid: UUID):
        await self._choice_repository.delete(uuid)

    async def update(self, payload: ChoiceSchema):
        await self._choice_repository.update(payload)

    async def delete_choice_by_user_id(self, user_id: UUID):
        await self._choice_repository.delete_by_user_id(user_id)
