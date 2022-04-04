import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.mf_calculation import OutMfCalculationSchema, InMfCalculationSchema, MfCalculationSchemaBase, MfCalculationSchema
from app.service.mf_calculation import MfCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_mf_calculation(payload: InMfCalculationSchema, db: AsyncSession = Depends(get_db)):
    mf_calculation_service = MfCalculationService(db)
    mf_calculation = await mf_calculation_service.create(payload)
    return mf_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_mf_calculation(payload: MfCalculationSchema, db: AsyncSession = Depends(get_db)):
    mf_calculation_service = MfCalculationService(db)
    await mf_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_mf_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    mf_calculation_service = MfCalculationService(db)
    mf_calculation = await mf_calculation_service.get_by_id(uuid)
    return mf_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_mf_calculation(db: AsyncSession = Depends(get_db)):
    mf_calculation_service = MfCalculationService(db)
    mf_calculation = await mf_calculation_service.get_all()
    return mf_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_mf_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    mf_calculation_service = MfCalculationService(db)
    await mf_calculation_service.delete(uuid)

    