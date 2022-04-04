import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.marital_status import MaritalStatusRepository
from app.models.schema.marital_status import OutMaritalStatusSchema, MaritalStatusSchema, InMaritalStatusSchema

logger = logging.getLogger(__name__)


class MaritalStatusService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._marital_status_repository = MaritalStatusRepository(self._db_session)

    async def create(self, payload: InMaritalStatusSchema):
        marital_status = await self._marital_status_repository.create(payload)

        return marital_status

    async def get_by_id(self, uuid: UUID):
        marital_status = await self._marital_status_repository.get_by_id(uuid)
        return marital_status

    async def get_all(self):
        marital_status = await self._marital_status_repository.get_all()
        return marital_status

    async def delete(self, uuid: UUID):
        await self._marital_status_repository.delete(uuid)

    async def update(self, payload: MaritalStatusSchema):
        await self._marital_status_repository.update(payload)

    