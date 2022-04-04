from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.relation_type import RelationType
from app.models.schema.relation_type import (
    RelationTypeSchemaBase,
    RelationTypeSchema,
    InRelationTypeSchema,
)


class RelationTypeRepository(
    BaseRepository[RelationTypeSchemaBase, RelationTypeSchema, RelationType]
):
    @property
    def _in_schema(self) -> Type[RelationTypeSchemaBase]:
        return InRelationTypeSchema

    @property
    def _schema(self) -> Type[RelationTypeSchema]:
        return RelationTypeSchema

    @property
    def _table(self) -> Type[RelationType]:
        return RelationType
