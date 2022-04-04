import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_client_occupation_code import (
    BseClientOccupationCodeRepository,
)
from app.models.schema.bse_client_occupation_code import (
    OutBseClientOccupationCodeSchema,
    InBseClientOccupationCodeSchema,
    BseClientOccupationCodeSchema,
)

logger = logging.getLogger(__name__)


class BseClientOccupationCodeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_client_occupation_code_repository = BseClientOccupationCodeRepository(self._db_session)

    async def create(
            self, payload: InBseClientOccupationCodeSchema
    ):
        bse_client_occupation_code = await self._bse_client_occupation_code_repository.create(
            payload
        )

        return bse_client_occupation_code

    async def get_by_id(self, uuid: UUID) -> OutBseClientOccupationCodeSchema:
        bse_client_occupation_code = (
            await self._bse_client_occupation_code_repository.get_by_id(uuid)
        )
        return bse_client_occupation_code

    async def get_all(self):
        bse_client_occupation_code = (
            await self._bse_client_occupation_code_repository.get_all()
        )
        return bse_client_occupation_code

    async def delete(self, uuid: UUID):
        await self._bse_client_occupation_code_repository.delete(uuid)

    async def update(self, payload: BseClientOccupationCodeSchema):
        await self._bse_client_occupation_code_repository.update(payload)

    async def delete_bse_client_occupation_code_by_user_id(self, user_id: UUID):
        await self._bse_client_occupation_code_repository.delete_by_user_id(user_id)
