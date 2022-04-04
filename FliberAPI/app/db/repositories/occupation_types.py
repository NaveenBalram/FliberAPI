from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.occupation_types import OccupationTypes
from app.models.schema.occupation_types import (
    OccupationTypesSchemaBase,
    OccupationTypesSchema,
    InOccupationTypesSchema,
)


class OccupationTypesRepository(
    BaseRepository[OccupationTypesSchemaBase, OccupationTypesSchema, OccupationTypes]
):
    @property
    def _in_schema(self) -> Type[OccupationTypesSchemaBase]:
        return InOccupationTypesSchema

    @property
    def _schema(self) -> Type[OccupationTypesSchema]:
        return OccupationTypesSchema

    @property
    def _table(self) -> Type[OccupationTypes]:
        return OccupationTypes
