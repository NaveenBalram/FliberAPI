from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.corpus_status import CorpusStatus
from app.models.schema.corpus_status import (
    CorpusStatusSchemaBase,
    CorpusStatusSchema,
    InCorpusStatusSchema,
)


class CorpusStatusRepository(
    BaseRepository[CorpusStatusSchemaBase, CorpusStatusSchema, CorpusStatus]
):
    @property
    def _in_schema(self) -> Type[CorpusStatusSchemaBase]:
        return InCorpusStatusSchema

    @property
    def _schema(self) -> Type[CorpusStatusSchema]:
        return CorpusStatusSchema

    @property
    def _table(self) -> Type[CorpusStatus]:
        return CorpusStatus
