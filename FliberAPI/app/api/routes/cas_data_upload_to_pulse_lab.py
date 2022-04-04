import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.cas_data_upload_to_pulse_lab import InCasDataUploadToPulseLabSchema, \
    CasDataUploadToPulseLabSchema
from app.service.cas_data_upload_to_pulse_lab import CasDataUploadToPulseLabService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_cas_data_upload_to_pulse_lab(payload: InCasDataUploadToPulseLabSchema,
                                              db: AsyncSession = Depends(get_db)):
    cas_data_upload_to_pulse_lab_service = CasDataUploadToPulseLabService(db)
    cas_data_upload_to_pulse_lab = await cas_data_upload_to_pulse_lab_service.create(payload)
    return cas_data_upload_to_pulse_lab


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_cas_data_upload_to_pulse_lab(payload: CasDataUploadToPulseLabSchema,
                                              db: AsyncSession = Depends(get_db)):
    cas_data_upload_to_pulse_lab_service = CasDataUploadToPulseLabService(db)
    await cas_data_upload_to_pulse_lab_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_cas_data_upload_to_pulse_lab(uuid: UUID, db: AsyncSession = Depends(get_db)):
    cas_data_upload_to_pulse_lab_service = CasDataUploadToPulseLabService(db)
    cas_data_upload_to_pulse_lab = await cas_data_upload_to_pulse_lab_service.get_by_id(uuid)
    return cas_data_upload_to_pulse_lab


@router.get("/", status_code=status.HTTP_200_OK)
async def get_cas_data_upload_to_pulse_lab(db: AsyncSession = Depends(get_db)):
    cas_data_upload_to_pulse_lab_service = CasDataUploadToPulseLabService(db)
    cas_data_upload_to_pulse_lab = await cas_data_upload_to_pulse_lab_service.get_all()
    return cas_data_upload_to_pulse_lab


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_cas_data_upload_to_pulse_lab(uuid: UUID, db: AsyncSession = Depends(get_db)):
    cas_data_upload_to_pulse_lab_service = CasDataUploadToPulseLabService(db)
    await cas_data_upload_to_pulse_lab_service.delete(uuid)


@router.get("/by/{user_id}", status_code=status.HTTP_200_OK)
async def get_cas_data_upload_to_pulse_lab_by_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    cas_data_upload_to_pulse_lab_service = CasDataUploadToPulseLabService(db)
    cas_data_upload_to_pulse_lab = await cas_data_upload_to_pulse_lab_service.get_by_user_id(user_id)
    return cas_data_upload_to_pulse_lab
