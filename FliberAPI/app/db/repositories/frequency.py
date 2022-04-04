from typing import Type

from sqlalchemy.future import select

from app.db.errors import DoesNotExist
from app.db.repositories.base import BaseRepository
from app.db.tables.frequency import Frequency
from app.models.schema.frequency import (
    FrequencySchemaBase,
    FrequencySchema,
    InFrequencySchema,
)


class FrequencyRepository(
    BaseRepository[FrequencySchemaBase, FrequencySchema, Frequency]
):
    @property
    def _in_schema(self) -> Type[FrequencySchemaBase]:
        return InFrequencySchema

    @property
    def _schema(self) -> Type[FrequencySchema]:
        return FrequencySchema

    @property
    def _table(self) -> Type[Frequency]:
        return Frequency

    async def get_by_name(self, kwargs):
        print("-----------------")
        print(kwargs)
        print("-----------------")
        result = await self._db_session.execute(
            select(self._table.Value).where(self._table.Name == kwargs["Name"])
        )

        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])
        if not return_items:
            raise DoesNotExist(f"Data does not exist")
        return return_items
