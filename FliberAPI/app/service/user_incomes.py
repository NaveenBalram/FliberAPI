import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user_incomes import UserIncomesRepository
from app.models.schema.user_incomes import (
    UserIncomesSchema,
    UserIncomesSchemaBase,
)

logger = logging.getLogger(__name__)


class UserIncomesService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_incomes_repository = UserIncomesRepository(self._db_session)

    async def create(self, payload: UserIncomesSchemaBase):
        user_incomes = await self._user_incomes_repository.create(payload)

        return user_incomes

    async def get_by_id(self, uuid: UUID):
        user_incomes = await self._user_incomes_repository.get_by_id(uuid)
        return user_incomes

    async def get_all(self):
        user_incomes = await self._user_incomes_repository.get_all()
        return user_incomes

    async def delete(self, uuid: UUID):
        await self._user_incomes_repository.delete(uuid)

    async def update(self, payload: UserIncomesSchema):
        await self._user_incomes_repository.update(payload)

    async def get_by_user_id(self, user_id: UUID):
        # return the user income data received from the function.
        return await self._user_incomes_repository.get_user_income_by_id(user_id)

    async def delete_user_incomes_by_user_id(self, user_id: UUID):
        await self._user_incomes_repository.delete_by_user_id(user_id)
