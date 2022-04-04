import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.advisor import AdvisorRepository
from app.models.schema.advisor import InAdvisorSchema, AdvisorSchema

logger = logging.getLogger(__name__)


class AdvisorService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._advisor_repository = AdvisorRepository(self._db_session)

    async def create(self, payload: InAdvisorSchema):
        advisor = await self._advisor_repository.create(payload)
        return advisor

    async def get_by_id(self, advisor_id: UUID):
        advisor = await self._advisor_repository.get_by_id(advisor_id)
        return advisor

    async def get_all(self):
        return await self._advisor_repository.get_all()

    async def delete(self, advisor_id: UUID):
        advisor_repository = AdvisorRepository(self._db_session)
        await advisor_repository.delete(advisor_id)

    async def update(self, payload: AdvisorSchema):
        await self._advisor_repository.update(payload)

    async def delete_advisor_by_user_id(self, user_id: UUID):
        await self._advisor_repository.delete_by_user_id(user_id)
