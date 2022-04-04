from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.areas_of_concerns import AreasOfConcerns
from app.models.schema.areas_of_concerns import (
    AreasOfConcernsSchemaBase,
    AreasOfConcernsSchema,
    InAreasOfConcernsSchema,
)


class AreasOfConcernsRepository(
    BaseRepository[AreasOfConcernsSchemaBase, AreasOfConcernsSchema, AreasOfConcerns]
):
    @property
    def _in_schema(self) -> Type[AreasOfConcernsSchemaBase]:
        return InAreasOfConcernsSchema

    @property
    def _schema(self) -> Type[AreasOfConcernsSchema]:
        return AreasOfConcernsSchema

    @property
    def _table(self) -> Type[AreasOfConcerns]:
        return AreasOfConcerns
