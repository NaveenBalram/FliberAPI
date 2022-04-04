from typing import Type

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.rate import Rate
from app.models.schema.rate import RateSchemaBase, RateSchema, InRateSchema


class RateRepository(BaseRepository[RateSchemaBase, RateSchema, Rate]):
    @property
    def _in_schema(self) -> Type[RateSchemaBase]:
        return InRateSchema

    @property
    def _schema(self) -> Type[RateSchema]:
        return RateSchema

    @property
    def _table(self) -> Type[Rate]:
        return Rate

    async def get_all_rate(self):
        result = await self._db_session.execute(select(self._table.Percentage))
        return_items = []
        for item in result.fetchall():
            return_items.append(item)
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items
