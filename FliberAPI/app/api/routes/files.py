from uuid import UUID

from fastapi import APIRouter, File, UploadFile, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies.db import get_db
from app.service.bse_client_code import BseClientCodeService
from app.service.cas_data_upload_from_pulse_lab import CasDataUploadFromPulseLabService

router = APIRouter()


@router.post("/upload/signature")
async def create_upload_file(
    user_id: UUID, image: UploadFile = File(...), db: AsyncSession = Depends(get_db)
):
    """ api to save signature """
    bse_user_account_service = BseClientCodeService(db)
    return await bse_user_account_service.upload_file(user_id, image)


@router.post("/upload/cas/pdf")
async def create_upload_file(
    user_id: UUID, image: UploadFile = File(...), db: AsyncSession = Depends(get_db)
):
    """ api to save signature """
    cas_service = CasDataUploadFromPulseLabService(db)
    return await cas_service.upload_file(user_id, image)
