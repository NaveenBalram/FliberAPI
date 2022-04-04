import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bucket import BucketRepository
from app.models.schema.bucket import InBucketSchema, BucketSchema

logger = logging.getLogger(__name__)


class BucketService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bucket_repository = BucketRepository(self._db_session)

    async def create(self, payload: InBucketSchema):
        bucket = await self._bucket_repository.create(payload)

        return bucket

    async def get_by_id(self, gender_id: UUID):
        bucket = await self._bucket_repository.get_by_id(gender_id)
        return bucket

    async def get_all(self):
        bucket = await self._bucket_repository.get_all()
        return bucket

    async def delete(self, gender_id: UUID):
        await self._bucket_repository.delete(gender_id)

    async def update(self, payload: BucketSchema):
        await self._bucket_repository.update(payload)

    async def delete_bucket_by_user_id(self, user_id: UUID):
        await self._bucket_repository.delete_by_user_id(user_id)
