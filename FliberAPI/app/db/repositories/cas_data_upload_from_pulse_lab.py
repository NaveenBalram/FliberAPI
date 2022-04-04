from typing import Type

import uuid
from sqlalchemy import delete, insert

from app.db.repositories.base import BaseRepository
from app.db.tables.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLab
from app.models.schema.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLabSchemaBase, \
    CasDataUploadFromPulseLabSchema, InCasDataUploadFromPulseLabSchema


class CasDataUploadFromPulseLabRepository(
    BaseRepository[CasDataUploadFromPulseLabSchemaBase, CasDataUploadFromPulseLabSchema, CasDataUploadFromPulseLab]):
    @property
    def _in_schema(self) -> Type[CasDataUploadFromPulseLabSchemaBase]:
        return InCasDataUploadFromPulseLabSchema

    @property
    def _schema(self) -> Type[CasDataUploadFromPulseLabSchema]:
        return CasDataUploadFromPulseLabSchema

    @property
    def _table(self) -> Type[CasDataUploadFromPulseLab]:
        return CasDataUploadFromPulseLab

    async def bulk_create(self, payload: list[CasDataUploadFromPulseLabSchema]):
        result = []
        flag = True
        for data in payload:
            if flag:
                stmt = (delete(self._table).where(self._table.UserId == data.UserId))
                await self._db_session.execute(stmt)
                await self._db_session.commit()
                flag = False

            data = data.__dict__
            data["Id"] = uuid.uuid4()
            result.append(data)

        await self._db_session.execute(insert(self._table).values(result))
        await self._db_session.commit()
        return result
