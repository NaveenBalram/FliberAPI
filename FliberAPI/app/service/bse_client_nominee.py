import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.repositories.bse_client_nominee import BseClientNomineeRepository
from app.models.schema.bse_client_nominee import (
    InBseClientNomineeSchema,
    BseClientNomineeSchema,
)

logger = logging.getLogger(__name__)


class BseClientNomineeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_client_nominee_repository = BseClientNomineeRepository(self._db_session)

    async def create(
            self, payload: InBseClientNomineeSchema
    ):
        account_type_exist = await self._bse_client_nominee_repository.check_exist(payload.UserId,
                                                                                   payload.NomineeNumber)
        if account_type_exist:
            return JSONResponse({"exception": "NomineeNumberExist",
                                 "detail": f"AccountTypeNumber {payload.NomineeNumber} already registered"},
                                status_code=400)
        bse_client_nominee = await self._bse_client_nominee_repository.create(payload)

        return bse_client_nominee

    async def get_by_id(self, uuid: UUID):
        bse_client_nominee = await self._bse_client_nominee_repository.get_by_id(uuid)
        return bse_client_nominee

    async def get_all(self):
        bse_client_nominee = await self._bse_client_nominee_repository.get_all()
        return bse_client_nominee

    async def delete(self, uuid: UUID):
        await self._bse_client_nominee_repository.delete(uuid)

    async def update(self, payload: BseClientNomineeSchema):
        await self._bse_client_nominee_repository.update(payload)

    async def delete_by_user_id(self, user_id: UUID):
        await self._bse_client_nominee_repository.delete(user_id)

    async def delete_bse_client_nominee_by_user_id(self, user_id: UUID):
        await self._bse_client_nominee_repository.delete_by_user_id(user_id)
