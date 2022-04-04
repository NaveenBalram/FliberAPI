from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.source_of_wealth import SourceOfWealth
from app.models.schema.source_of_wealth import (
    SourceOfWealthSchemaBase,
    SourceOfWealthSchema,
    InSourceOfWealthSchema,
)


class SourceOfWealthRepository(
    BaseRepository[SourceOfWealthSchemaBase, SourceOfWealthSchema, SourceOfWealth]
):
    @property
    def _in_schema(self) -> Type[SourceOfWealthSchemaBase]:
        return InSourceOfWealthSchema

    @property
    def _schema(self) -> Type[SourceOfWealthSchema]:
        return SourceOfWealthSchema

    @property
    def _table(self) -> Type[SourceOfWealth]:
        return SourceOfWealth
