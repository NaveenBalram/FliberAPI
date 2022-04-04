from typing import Type

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.bucket import Bucket
from app.models.schema.bucket import InBucketSchema, BucketSchema


class BucketRepository(BaseRepository[InBucketSchema, BucketSchema, Bucket]):
    @property
    def _in_schema(self) -> Type[InBucketSchema]:
        return InBucketSchema

    @property
    def _schema(self) -> Type[BucketSchema]:
        return BucketSchema

    @property
    def _table(self) -> Type[Bucket]:
        return Bucket

    async def get_all_rate(self):
        result = await self._db_session.execute(
            select(self._table.Rate, self._table.Years)
        )
        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items
