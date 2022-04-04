from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.nominee_relation import NomineeRelation
from app.models.schema.nominee_relation import (
    NomineeRelationSchemaBase,
    NomineeRelationSchema,
    InNomineeRelationSchema,
)


class NomineeRelationRepository(
    BaseRepository[NomineeRelationSchemaBase, NomineeRelationSchema, NomineeRelation]
):
    @property
    def _in_schema(self) -> Type[NomineeRelationSchemaBase]:
        return InNomineeRelationSchema

    @property
    def _schema(self) -> Type[NomineeRelationSchema]:
        return NomineeRelationSchema

    @property
    def _table(self) -> Type[NomineeRelation]:
        return NomineeRelation
