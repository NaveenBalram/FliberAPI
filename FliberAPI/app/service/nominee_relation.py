import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.nominee_relation import NomineeRelationRepository
from app.models.schema.nominee_relation import (
    InNomineeRelationSchema,
    NomineeRelationSchema,
)

logger = logging.getLogger(__name__)


class NomineeRelationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._nominee_relation_repository = NomineeRelationRepository(self._db_session)

    async def create(
            self, payload: InNomineeRelationSchema
    ):
        nominee_relation = await self._nominee_relation_repository.create(payload)

        return nominee_relation

    async def get_by_id(self, uuid: UUID):
        nominee_relation = await self._nominee_relation_repository.get_by_id(uuid)
        return nominee_relation

    async def get_all(self):
        nominee_relation = await self._nominee_relation_repository.get_all()
        return nominee_relation

    async def delete(self, uuid: UUID):
        await self._nominee_relation_repository.delete(uuid)

    async def update(self, payload: NomineeRelationSchema):
        await self._nominee_relation_repository.update(payload)

    async def delete_nominee_relation_by_user_id(self, user_id: UUID):
        await self._nominee_relation_repository.delete_by_user_id(user_id)
