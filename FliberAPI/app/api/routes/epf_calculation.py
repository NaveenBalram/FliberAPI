import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.epf_calculation import InEpfCalculationSchema, EpfCalculationSchema
from app.service.epf_calculation import EpfCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_epf_calculation(payload: InEpfCalculationSchema, db: AsyncSession = Depends(get_db)):
    epf_calculation_service = EpfCalculationService(db)
    epf_calculation = await epf_calculation_service.create(payload)
    return epf_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_epf_calculation(payload: EpfCalculationSchema, db: AsyncSession = Depends(get_db)):
    epf_calculation_service = EpfCalculationService(db)
    await epf_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_epf_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    epf_calculation_service = EpfCalculationService(db)
    epf_calculation = await epf_calculation_service.get_by_id(uuid)
    return epf_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_epf_calculation(db: AsyncSession = Depends(get_db)):
    epf_calculation_service = EpfCalculationService(db)
    epf_calculation = await epf_calculation_service.get_all()
    return epf_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_epf_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    epf_calculation_service = EpfCalculationService(db)
    await epf_calculation_service.delete(uuid)
