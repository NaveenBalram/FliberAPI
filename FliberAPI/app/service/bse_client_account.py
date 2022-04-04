import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.repositories.bse_client_account import BseClientAccountRepository
from app.models.schema.bse_client_account import (
    InBseClientAccountSchema,
    BseClientAccountSchema,
)

logger = logging.getLogger(__name__)


class BseClientAccountService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_client_account_repository = BseClientAccountRepository(self._db_session)

    async def create(
            self, payload: InBseClientAccountSchema
    ):
        account_type_exist = await self._bse_client_account_repository.check_exist(payload.UserId,
                                                                                   payload.AccountTypeNumber)
        if account_type_exist:
            return JSONResponse({"exception": "AccountTypeNumberExist",
                                 "detail": f"AccountTypeNumber {payload.AccountTypeNumber} already registered"},
                                status_code=400)
        bse_client_account = await self._bse_client_account_repository.create(payload)

        return bse_client_account

    async def get_by_id(self, uuid: UUID):
        bse_client_account = await self._bse_client_account_repository.get_by_id(uuid)
        return bse_client_account

    async def get_all(self):
        bse_client_account = await self._bse_client_account_repository.get_all()
        return bse_client_account

    async def delete(self, uuid: UUID):
        await self._bse_client_account_repository.delete(uuid)

    async def update(self, payload: BseClientAccountSchema):
        await self._bse_client_account_repository.update(payload)

    async def delete_by_user_id(self, user_id: UUID):
        bse_client_nominee_repository = BseClientAccountRepository(self._db_session)
        await bse_client_nominee_repository.delete(user_id)

    async def update_by_user(self, payload: BseClientAccountSchema):
        await self._bse_client_account_repository.update_by_user(payload)

    async def delete_bse_client_account_by_user_id(self, user_id: UUID):
        await self._bse_client_account_repository.delete_by_user_id(user_id)
