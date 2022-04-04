import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.corpus_status import CorpusStatusRepository
from app.models.schema.corpus_status import (
    OutCorpusStatusSchema,
    InCorpusStatusSchema,
    CorpusStatusSchema,
)

logger = logging.getLogger(__name__)


class CorpusStatusService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._corpus_status_repository = CorpusStatusRepository(self._db_session)

    async def create(self, payload: InCorpusStatusSchema):
        corpus_status = await self._corpus_status_repository.create(payload)

        return corpus_status

    async def get_by_id(self, uuid: UUID) -> OutCorpusStatusSchema:
        corpus_status = await self._corpus_status_repository.get_by_id(uuid)
        return corpus_status

    async def get_all(self):
        corpus_status = await self._corpus_status_repository.get_all()
        return corpus_status

    async def delete(self, uuid: UUID):
        await self._corpus_status_repository.delete(uuid)

    async def update(self, payload: CorpusStatusSchema):
        await self._corpus_status_repository.update(payload)

    async def delete_corpus_status_by_user_id(self, user_id: UUID):
        await self._corpus_status_repository.delete_by_user_id(user_id)
