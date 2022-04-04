import logging
import shutil
from uuid import UUID

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import FliberUrl
from app.db.repositories.cas_data_upload_to_pulse_lab import CasDataUploadToPulseLabRepository
from app.models.schema.cas_data_upload_to_pulse_lab import CasDataUploadToPulseLabSchema, \
    InCasDataUploadToPulseLabSchema

logger = logging.getLogger(__name__)


class CasDataUploadToPulseLabService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._cas_data_upload_to_pulse_lab_repository = CasDataUploadToPulseLabRepository(self._db_session)

    async def create(self, payload: InCasDataUploadToPulseLabSchema):

        url = "https://alchemy-service.pulselabs.co.in/rta-upload/upload"
        files = {'file': open(f'files/cas_files/{payload.CasFile.rsplit("/", maxsplit=1)[-1]}', 'rb')}
        requests.post(url, files=files, data={"password": payload.Password})
        cas_data_upload_to_pulse_lab = await self._cas_data_upload_to_pulse_lab_repository.create(payload)

        return cas_data_upload_to_pulse_lab

    async def get_by_id(self, uuid: UUID):
        cas_data_upload_to_pulse_lab = await self._cas_data_upload_to_pulse_lab_repository.get_by_id(uuid)
        return cas_data_upload_to_pulse_lab

    async def get_all(self):
        cas_data_upload_to_pulse_lab = await self._cas_data_upload_to_pulse_lab_repository.get_all()
        return cas_data_upload_to_pulse_lab

    async def delete(self, uuid: UUID):
        await self._cas_data_upload_to_pulse_lab_repository.delete(uuid)

    async def update(self, payload: CasDataUploadToPulseLabSchema):
        await self._cas_data_upload_to_pulse_lab_repository.update(payload)

    async def get_by_user_id(self, user_id):
        await self._cas_data_upload_to_pulse_lab_repository.get_by_user_id(user_id)

    async def upload_file(self, image):
        try:
            with open(f"images/signature/{image.filename}", "wb") as buffer:
                shutil.copyfileobj(image.file, buffer)

            return f"{FliberUrl.url}/signature/{image.filename}"

        except Exception as e:
            return f"File Upload Failed: {e}"
