from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.cas_data_upload_to_pulse_lab import CasDataUploadToPulseLab
from app.models.schema.cas_data_upload_to_pulse_lab import CasDataUploadToPulseLabSchemaBase, CasDataUploadToPulseLabSchema, CasDataUploadToPulseLabSchema, InCasDataUploadToPulseLabSchema


class CasDataUploadToPulseLabRepository(BaseRepository[CasDataUploadToPulseLabSchemaBase, CasDataUploadToPulseLabSchema, CasDataUploadToPulseLab]):
    @property
    def _in_schema(self) -> Type[CasDataUploadToPulseLabSchemaBase]:
        return InCasDataUploadToPulseLabSchema

    @property
    def _schema(self) -> Type[CasDataUploadToPulseLabSchema]:
        return CasDataUploadToPulseLabSchema

    @property
    def _table(self) -> Type[CasDataUploadToPulseLab]:
        return CasDataUploadToPulseLab
