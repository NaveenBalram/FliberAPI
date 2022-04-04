import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.signzy_users import SignzyUsersRepository
from app.models.schema.signzy_users import (
    InSignzyUsersSchema,
    SignzyUsersSchema,
)

logger = logging.getLogger(__name__)


class SignzyUsersService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._signzy_users_repository = SignzyUsersRepository(self._db_session)

    async def create(self, payload: InSignzyUsersSchema):
        signzy_users = await self._signzy_users_repository.create(payload)

        return signzy_users

    async def get_by_id(self, uuid: UUID):
        signzy_users = await self._signzy_users_repository.get_by_id(uuid)
        return signzy_users

    async def get_all(self):
        signzy_users = await self._signzy_users_repository.get_all()
        return signzy_users

    async def delete(self, uuid: UUID):
        await self._signzy_users_repository.delete(uuid)

    async def update(self, payload: SignzyUsersSchema):
        await self._signzy_users_repository.update(payload)

    async def delete_signzy_users_by_user_id(self, user_id: UUID):
        await self._signzy_users_repository.delete_by_user_id(user_id)
