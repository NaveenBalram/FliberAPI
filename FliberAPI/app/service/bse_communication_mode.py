import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_communication_mode import BseCommunicationModeRepository
from app.models.schema.bse_communication_mode import (
    OutBseCommunicationModeSchema,
    InBseCommunicationModeSchema,
    BseCommunicationModeSchema,
)

logger = logging.getLogger(__name__)


class BseCommunicationModeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_communication_mode_repository = BseCommunicationModeRepository(self._db_session)

    async def create(
            self, payload: InBseCommunicationModeSchema
    ):
        bse_communication_mode = await self._bse_communication_mode_repository.create(payload)
        return bse_communication_mode

    async def get_by_id(self, uuid: UUID) -> OutBseCommunicationModeSchema:
        bse_communication_mode = await self._bse_communication_mode_repository.get_by_id(uuid)
        return bse_communication_mode

    async def get_all(self):
        bse_communication_mode = await self._bse_communication_mode_repository.get_all()
        return bse_communication_mode

    async def delete(self, uuid: UUID):
        await self._bse_communication_mode_repository.delete(uuid)

    async def update(self, payload: BseCommunicationModeSchema):
        await self._bse_communication_mode_repository.update(payload)

    async def delete_bse_communication_mode_by_user_id(self, user_id: UUID):
        await self._bse_communication_mode_repository.delete_by_user_id(user_id)
