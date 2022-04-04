import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.users_re_balance_sheet import UsersReBalanceSheetRepository
from app.models.schema.users_re_balance_sheet import (
    UsersReBalanceSheetSchema,
    InUsersReBalanceSheetSchema,
)

logger = logging.getLogger(__name__)


class UsersReBalanceSheetService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._users_re_balance_sheet_repository = UsersReBalanceSheetRepository(self._db_session)

    async def create(
            self, payload: InUsersReBalanceSheetSchema
    ):
        users_re_balance_sheet = await self._users_re_balance_sheet_repository.create(payload)

        return users_re_balance_sheet

    async def get_by_id(self, uuid: UUID):
        users_re_balance_sheet = await self._users_re_balance_sheet_repository.get_by_id(uuid)
        return users_re_balance_sheet

    async def get_all(self):
        users_re_balance_sheet = await self._users_re_balance_sheet_repository.get_all()
        return users_re_balance_sheet

    async def delete(self, uuid: UUID):
        await self._users_re_balance_sheet_repository.delete(uuid)

    async def update(self, payload: UsersReBalanceSheetSchema):
        await self._users_re_balance_sheet_repository.update(payload)
