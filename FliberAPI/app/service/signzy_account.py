import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.signzy_account import SignzyAccountRepository
from app.models.schema.signzy_account import (
    InSignzyAccountSchema,
    SignzyAccountSchema,
)

logger = logging.getLogger(__name__)


class SignzyAccountService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._signzy_account_repository = SignzyAccountRepository(self._db_session)

    async def create(self, payload: InSignzyAccountSchema):
        signzy_account = await self._signzy_account_repository.create(payload)

        return signzy_account

    async def get_by_id(self, uuid: UUID):
        signzy_account = await self._signzy_account_repository.get_by_id(uuid)
        return signzy_account

    async def get_all(self):
        signzy_account = await self._signzy_account_repository.get_all()
        return signzy_account

    async def delete(self, uuid: UUID):
        await self._signzy_account_repository.delete(uuid)

    async def update(self, payload: SignzyAccountSchema):
        await self._signzy_account_repository.update(payload)

    async def delete_signzy_account_by_user_id(self, user_id: UUID):
        await self._signzy_account_repository.delete_by_user_id(user_id)
