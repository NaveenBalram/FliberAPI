import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.relation_type import RelationTypeRepository
from app.models.schema.relation_type import (
    InRelationTypeSchema,
    RelationTypeSchema,
)

logger = logging.getLogger(__name__)


class RelationTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._relation_type_repository = RelationTypeRepository(self._db_session)

    async def create(self, payload: InRelationTypeSchema):
        relation_type = await self._relation_type_repository.create(payload)

        return relation_type

    async def get_by_id(self, uuid: UUID):
        relation_type = await self._relation_type_repository.get_by_id(uuid)
        return relation_type

    async def get_all(self):
        relation_type = await self._relation_type_repository.get_all()
        return relation_type

    async def delete(self, uuid: UUID):
        await self._relation_type_repository.delete(uuid)

    async def update(self, payload: RelationTypeSchema):
        await self._relation_type_repository.update(payload)

    async def delete_relation_type_by_user_id(self, user_id: UUID):
        await self._relation_type_repository.delete_by_user_id(user_id)
