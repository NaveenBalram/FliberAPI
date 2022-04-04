from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.daily_nav_data import DailyNavData
from app.models.schema.daily_nav_data import (
    DailyNavDataSchemaBase,
    DailyNavDataSchema,
    DailyNavDataSchema,
)


class DailyNavDataRepository(
    BaseRepository[DailyNavDataSchemaBase, DailyNavDataSchema, DailyNavData]
):
    @property
    def _in_schema(self) -> Type[DailyNavDataSchemaBase]:
        return InDailyNavDataSchema

    @property
    def _schema(self) -> Type[DailyNavDataSchema]:
        return DailyNavDataSchema

    @property
    def _table(self) -> Type[DailyNavData]:
        return DailyNavData
