import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.rr_score_result import RrScoreResultRepository
from app.models.schema.rr_score_result import OutRrScoreResultSchema, RrScoreResultSchema, InRrScoreResultSchema

logger = logging.getLogger(__name__)


class RrScoreResultService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._rr_score_result_repository = RrScoreResultRepository(self._db_session)

    async def create(self, payload: InRrScoreResultSchema):
        rr_score_result = await self._rr_score_result_repository.create(payload)

        return rr_score_result

    async def get_by_id(self, uuid: UUID):
        rr_score_result = await self._rr_score_result_repository.get_by_id(uuid)
        return rr_score_result

    async def get_all(self):
        rr_score_result = await self._rr_score_result_repository.get_all()
        return rr_score_result

    async def delete(self, uuid: UUID):
        await self._rr_score_result_repository.delete(uuid)

    async def update(self, payload: RrScoreResultSchema):
        await self._rr_score_result_repository.update(payload)

    async def get_by_user_id(self, user_id):
        return await self._rr_score_result_repository.get_by_user_id(user_id)

