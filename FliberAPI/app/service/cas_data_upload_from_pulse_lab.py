import datetime
import logging
from uuid import UUID

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLabRepository
from app.models.schema.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLabSchema, \
    InCasDataUploadFromPulseLabSchema

logger = logging.getLogger(__name__)


class CasDataUploadFromPulseLabService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._cas_data_upload_from_pulse_lab_repository = CasDataUploadFromPulseLabRepository(self._db_session)

    async def create(self, payload: InCasDataUploadFromPulseLabSchema):
        cas_data_upload_from_pulse_lab = await self._cas_data_upload_from_pulse_lab_repository.create(payload)
        return cas_data_upload_from_pulse_lab

    async def get_by_id(self, uuid: UUID):
        cas_data_upload_from_pulse_lab = await self._cas_data_upload_from_pulse_lab_repository.get_by_id(uuid)
        return cas_data_upload_from_pulse_lab

    async def get_all(self):
        cas_data_upload_from_pulse_lab = await self._cas_data_upload_from_pulse_lab_repository.get_all()
        return cas_data_upload_from_pulse_lab

    async def delete(self, uuid: UUID):
        await self._cas_data_upload_from_pulse_lab_repository.delete(uuid)

    async def update(self, payload: CasDataUploadFromPulseLabSchema):
        await self._cas_data_upload_from_pulse_lab_repository.update(payload)

    async def generate(self, cas_data):
        url = "https://alchemy-service.pulselabs.co.in/rta_report/client_portfolio_consolidated"
        data = {
            "advisor_id": "ARN-110384" or cas_data.AdvisorId,
            "client_id": "1090364" or cas_data.ClientId,
            "sub_advisor_id": "" or cas_data.SubAdvisorId
        }

        cas = []

        result = requests.post(url, data=data).json()
        if result["message"] == 'No records found':
            return 'No records found'

        for items in result:
            cas_data = CasDataUploadFromPulseLabSchema(
                UserId=cas_data.UserId,
                ClientId=items.client_id,
                SchemeFolioNo=items.scheme_folio_no,
                SchemeName=items.scheme_name,
                SchemeCode=items.scheme_code,
                UnitBalance=items.unit_balance,
                CurrentValue=items.current_value,
                CreatedOn=datetime.datetime.now(),
                UpdatedOn=datetime.datetime.now(),
                IsDeleted=bool
            )

            cas.append(cas_data)

        return self._cas_data_upload_from_pulse_lab_repository.bulk_create(cas)



