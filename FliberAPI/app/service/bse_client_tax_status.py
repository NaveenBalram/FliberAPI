import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_client_tax_status import BseClientTaxStatusRepository
from app.models.schema.bse_client_tax_status import (
    OutBseClientTaxStatusSchema,
    InBseClientTaxStatusSchema,
    BseClientTaxStatusSchema,
)

logger = logging.getLogger(__name__)


class BseClientTaxStatusService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_client_tax_status_repository = BseClientTaxStatusRepository(self._db_session)

    async def create(
            self, payload: InBseClientTaxStatusSchema
    ):
        bse_client_tax_status = await self._bse_client_tax_status_repository.create(payload)

        return bse_client_tax_status

    async def get_by_id(self, uuid: UUID) -> OutBseClientTaxStatusSchema:
        bse_client_tax_status = await self._bse_client_tax_status_repository.get_by_id(uuid)
        return bse_client_tax_status

    async def get_all(self):
        bse_client_tax_status = await self._bse_client_tax_status_repository.get_all()
        return bse_client_tax_status

    async def delete(self, uuid: UUID):
        await self._bse_client_tax_status_repository.delete(uuid)

    async def update(self, payload: BseClientTaxStatusSchema):
        await self._bse_client_tax_status_repository.update(payload)

    async def delete_bse_client_tax_status_by_user_id(self, user_id: UUID):
        await self._bse_client_tax_status_repository.delete_by_user_id(user_id)
