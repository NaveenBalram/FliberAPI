import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.cas_upload import CasUploadRepository
from app.models.schema.cas_upload import CasUploadSchema, InCasUploadSchema
from app.service.cas_upload_logic.cas_upload import scrap_cas

logger = logging.getLogger(__name__)


class CasUploadService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._cas_upload_repository = CasUploadRepository(self._db_session)

    async def create(self, payload: InCasUploadSchema):
        cas_upload = await self._cas_upload_repository.create(payload)

        return cas_upload

    async def get_by_id(self, uuid: UUID):
        cas_upload = await self._cas_upload_repository.get_by_id(uuid)
        return cas_upload

    async def get_all(self):
        cas_upload = await self._cas_upload_repository.get_all()
        return cas_upload

    async def delete(self, uuid: UUID):
        await self._cas_upload_repository.delete(uuid)

    async def update(self, payload: CasUploadSchema):
        await self._cas_upload_repository.update(payload)

    def upload_cash(self, email_id, password):
        return scrap_cas(email_id, password)
