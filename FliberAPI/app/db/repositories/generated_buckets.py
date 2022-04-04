from typing import Type

from sqlalchemy import delete

from app.db.repositories.base import BaseRepository
from app.db.tables.generated_buckets import GeneratedBuckets
from app.models.schema.generated_buckets import (
    GeneratedBucketsSchemaBase,
    GeneratedBucketsSchema,
    InGeneratedBucketsSchema,
)


class GeneratedBucketsRepository(
    BaseRepository[GeneratedBucketsSchemaBase, GeneratedBucketsSchema, GeneratedBuckets]
):
    @property
    def _in_schema(self) -> Type[GeneratedBucketsSchemaBase]:
        return InGeneratedBucketsSchema

    @property
    def _schema(self) -> Type[GeneratedBucketsSchema]:
        return GeneratedBucketsSchema

    @property
    def _table(self) -> Type[GeneratedBuckets]:
        return GeneratedBuckets

    async def delete_buckets_by_user_id(self, user_id):
        return await self._db_session.execute(delete(self._table).where(self._table.UserId == user_id))


