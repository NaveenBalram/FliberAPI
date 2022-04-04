import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.cas_data_upload_from_pulse_lab import InCasDataUploadFromPulseLabSchema, \
    CasDataUploadFromPulseLabSchema, CasData
from app.service.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLabService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_cas_data_upload_from_pulse_lab(payload: InCasDataUploadFromPulseLabSchema,
                                                db: AsyncSession = Depends(get_db)):
    cas_data_upload_from_pulse_lab_service = CasDataUploadFromPulseLabService(db)
    cas_data_upload_from_pulse_lab = await cas_data_upload_from_pulse_lab_service.create(payload)
    return cas_data_upload_from_pulse_lab


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_cas_data_upload_from_pulse_lab(payload: CasDataUploadFromPulseLabSchema,
                                                db: AsyncSession = Depends(get_db)):
    cas_data_upload_from_pulse_lab_service = CasDataUploadFromPulseLabService(db)
    await cas_data_upload_from_pulse_lab_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_cas_data_upload_from_pulse_lab(uuid: UUID, db: AsyncSession = Depends(get_db)):
    cas_data_upload_from_pulse_lab_service = CasDataUploadFromPulseLabService(db)
    cas_data_upload_from_pulse_lab = await cas_data_upload_from_pulse_lab_service.get_by_id(uuid)
    return cas_data_upload_from_pulse_lab


@router.get("/", status_code=status.HTTP_200_OK)
async def get_cas_data_upload_from_pulse_lab(db: AsyncSession = Depends(get_db)):
    cas_data_upload_from_pulse_lab_service = CasDataUploadFromPulseLabService(db)
    cas_data_upload_from_pulse_lab = await cas_data_upload_from_pulse_lab_service.get_all()
    return cas_data_upload_from_pulse_lab


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_cas_data_upload_from_pulse_lab(uuid: UUID, db: AsyncSession = Depends(get_db)):
    cas_data_upload_from_pulse_lab_service = CasDataUploadFromPulseLabService(db)
    await cas_data_upload_from_pulse_lab_service.delete(uuid)


@router.post("/cas/data/", status_code=status.HTTP_200_OK)
async def get_cas_data_upload_from_pulse_lab(cas_data: CasData, db: AsyncSession = Depends(get_db)):
    cas_data_upload_from_pulse_lab_service = CasDataUploadFromPulseLabService(db)
    cas_data_upload_from_pulse_lab = await cas_data_upload_from_pulse_lab_service.generate(cas_data)
    return cas_data_upload_from_pulse_lab
