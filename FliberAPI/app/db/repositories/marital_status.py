from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.marital_status import MaritalStatus
from app.models.schema.marital_status import MaritalStatusSchemaBase, MaritalStatusSchema, InMaritalStatusSchema


class MaritalStatusRepository(BaseRepository[MaritalStatusSchemaBase, MaritalStatusSchema, MaritalStatus]):
    @property
    def _in_schema(self) -> Type[MaritalStatusSchemaBase]:
        return InMaritalStatusSchema

    @property
    def _schema(self) -> Type[MaritalStatusSchema]:
        return MaritalStatusSchema

    @property
    def _table(self) -> Type[MaritalStatus]:
        return MaritalStatus
