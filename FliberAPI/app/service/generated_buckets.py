import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.generated_buckets import GeneratedBucketsRepository
from app.models.schema.generated_buckets import (
    InGeneratedBucketsSchema,
    GeneratedBucketsSchema,
)

logger = logging.getLogger(__name__)


class GeneratedBucketsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._generated_buckets_repository = GeneratedBucketsRepository(self._db_session)

    async def create(
            self, payload: InGeneratedBucketsSchema
    ):
        generated_buckets = await self._generated_buckets_repository.create(payload)

        return generated_buckets

    async def get_by_id(self, uuid: UUID):
        generated_buckets = await self._generated_buckets_repository.get_by_id(uuid)
        return generated_buckets

    async def get_all(self):
        generated_buckets = await self._generated_buckets_repository.get_all()
        return generated_buckets

    async def delete(self, uuid: UUID):
        await self._generated_buckets_repository.delete(uuid)

    async def update(self, payload: GeneratedBucketsSchema):
        await self._generated_buckets_repository.update(payload)

    async def delete_generated_buckets_by_user_id(self, user_id: UUID):
        await self._generated_buckets_repository.delete_by_user_id(user_id)

    async def get_by_user_id(self, user_id):
        return await self._generated_buckets_repository.get_by_user_id(user_id)
