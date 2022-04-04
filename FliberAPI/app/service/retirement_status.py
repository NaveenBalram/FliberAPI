import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.retirement_status import RetirementStatusRepository
from app.models.schema.retirement_status import (
    InRetirementStatusSchema,
    RetirementStatusSchema,
)

logger = logging.getLogger(__name__)


class RetirementStatusService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._retirement_status_repository = RetirementStatusRepository(self._db_session)

    async def create(
            self, payload: InRetirementStatusSchema
    ):
        retirement_status = await self._retirement_status_repository.create(payload)

        return retirement_status

    async def get_by_id(self, uuid: UUID):
        retirement_status = await self._retirement_status_repository.get_by_id(uuid)
        return retirement_status

    async def get_all(self):
        retirement_status = await self._retirement_status_repository.get_all()
        return retirement_status

    async def delete(self, uuid: UUID):
        await self._retirement_status_repository.delete(uuid)

    async def update(self, payload: RetirementStatusSchema):
        await self._retirement_status_repository.update(payload)

    async def delete_retirement_status_by_user_id(self, user_id: UUID):
        await self._retirement_status_repository.delete_by_user_id(user_id)
