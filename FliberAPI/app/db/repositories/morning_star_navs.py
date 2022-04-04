from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.morning_star_navs import MorningStarNavs
from app.models.schema.morning_star_navs import (
    MorningStarNavsSchemaBase,
    MorningStarNavsSchema,
    MorningStarNavsSchema,
    InMorningStarNavsSchema,
)


class MorningStarNavsRepository(
    BaseRepository[MorningStarNavsSchemaBase, MorningStarNavsSchema, MorningStarNavs]
):
    @property
    def _in_schema(self) -> Type[MorningStarNavsSchemaBase]:
        return InMorningStarNavsSchema

    @property
    def _schema(self) -> Type[MorningStarNavsSchema]:
        return MorningStarNavsSchema

    @property
    def _table(self) -> Type[MorningStarNavs]:
        return MorningStarNavs
