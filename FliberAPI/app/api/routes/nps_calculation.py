import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.nps_calculation import OutNpsCalculationSchema, InNpsCalculationSchema, NpsCalculationSchemaBase, NpsCalculationSchema
from app.service.nps_calculation import NpsCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_nps_calculation(payload: InNpsCalculationSchema, db: AsyncSession = Depends(get_db)):
    nps_calculation_service = NpsCalculationService(db)
    nps_calculation = await nps_calculation_service.create(payload)
    return nps_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_nps_calculation(payload: NpsCalculationSchema, db: AsyncSession = Depends(get_db)):
    nps_calculation_service = NpsCalculationService(db)
    await nps_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_nps_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    nps_calculation_service = NpsCalculationService(db)
    nps_calculation = await nps_calculation_service.get_by_id(uuid)
    return nps_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_nps_calculation(db: AsyncSession = Depends(get_db)):
    nps_calculation_service = NpsCalculationService(db)
    nps_calculation = await nps_calculation_service.get_all()
    return nps_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_nps_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    nps_calculation_service = NpsCalculationService(db)
    await nps_calculation_service.delete(uuid)

    