from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.epfo_auto_fetch import EpfoAutoFetch
from app.models.schema.epfo_auto_fetch import EpfoAutoFetchSchemaBase, EpfoAutoFetchSchema, EpfoAutoFetchSchema, InEpfoAutoFetchSchema


class EpfoAutoFetchRepository(BaseRepository[EpfoAutoFetchSchemaBase, EpfoAutoFetchSchema, EpfoAutoFetch]):
    @property
    def _in_schema(self) -> Type[EpfoAutoFetchSchemaBase]:
        return InEpfoAutoFetchSchema

    @property
    def _schema(self) -> Type[EpfoAutoFetchSchema]:
        return EpfoAutoFetchSchema

    @property
    def _table(self) -> Type[EpfoAutoFetch]:
        return EpfoAutoFetch
