import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_state_code import BseStateCodeRepository
from app.models.schema.bse_state_code import (
    InBseStateCodeSchema,
    BseStateCodeSchema,
)

logger = logging.getLogger(__name__)


class BseStateCodeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_state_code_repository = BseStateCodeRepository(self._db_session)

    async def create(self, payload: InBseStateCodeSchema):
        bse_state_code = await self._bse_state_code_repository.create(payload)

        return bse_state_code

    async def get_by_id(self, uuid: UUID):
        bse_state_code = await self._bse_state_code_repository.get_by_id(uuid)
        return bse_state_code

    async def get_all(self):
        bse_state_code = await self._bse_state_code_repository.get_all()
        return bse_state_code

    async def delete(self, uuid: UUID):
        await self._bse_state_code_repository.delete(uuid)

    async def update(self, payload: BseStateCodeSchema):
        await self._bse_state_code_repository.update(payload)

    async def delete_bse_state_code_by_user_id(self, user_id: UUID):
        await self._bse_state_code_repository.delete_by_user_id(user_id)
