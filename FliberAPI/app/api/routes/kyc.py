import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.kyc import OutKycSchema, InKycSchema, KycSchema
from app.service.kyc import KycService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutKycSchema)
async def create_kyc(
    payload: InKycSchema, db: AsyncSession = Depends(get_db)
) -> OutKycSchema:
    """ api to save kyc data. """
    kyc_service = KycService(db)
    kyc = await kyc_service.create(payload)
    return kyc


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_kyc(payload: KycSchema, db: AsyncSession = Depends(get_db)):
    """ api to get kyc data. """
    kyc_service = KycService(db)
    await kyc_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutKycSchema)
async def get_kyc(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutKycSchema:
    """ api to get kyc data by id. """
    kyc_service = KycService(db)
    kyc = await kyc_service.get_by_id(uuid)
    return kyc


@router.get("/", status_code=status.HTTP_200_OK)
async def get_kyc(db: AsyncSession = Depends(get_db)):
    """ api to get kyc data. """
    kyc_service = KycService(db)
    kyc = await kyc_service.get_all()
    return kyc


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_kyc(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete kyc data by id. """
    kyc_service = KycService(db)
    await kyc_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_kyc_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete kyc data by user_id. """
    kyc_service = KycService(db)
    await kyc_service.delete(user_id)
