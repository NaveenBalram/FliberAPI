from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.cas_upload import CasUpload
from app.models.schema.cas_upload import CasUploadSchemaBase, CasUploadSchema, CasUploadSchema, InCasUploadSchema


class CasUploadRepository(BaseRepository[CasUploadSchemaBase, CasUploadSchema, CasUpload]):
    @property
    def _in_schema(self) -> Type[CasUploadSchemaBase]:
        return InCasUploadSchema

    @property
    def _schema(self) -> Type[CasUploadSchema]:
        return CasUploadSchema

    @property
    def _table(self) -> Type[CasUpload]:
        return CasUpload
