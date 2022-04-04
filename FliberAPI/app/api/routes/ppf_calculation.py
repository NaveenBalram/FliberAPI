import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.ppf_calculation import OutPpfCalculationSchema, InPpfCalculationSchema, PpfCalculationSchemaBase, PpfCalculationSchema
from app.service.ppf_calculation import PpfCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_ppf_calculation(payload: InPpfCalculationSchema, db: AsyncSession = Depends(get_db)):
    ppf_calculation_service = PpfCalculationService(db)
    ppf_calculation = await ppf_calculation_service.create(payload)
    return ppf_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_ppf_calculation(payload: PpfCalculationSchema, db: AsyncSession = Depends(get_db)):
    ppf_calculation_service = PpfCalculationService(db)
    await ppf_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_ppf_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    ppf_calculation_service = PpfCalculationService(db)
    ppf_calculation = await ppf_calculation_service.get_by_id(uuid)
    return ppf_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_ppf_calculation(db: AsyncSession = Depends(get_db)):
    ppf_calculation_service = PpfCalculationService(db)
    ppf_calculation = await ppf_calculation_service.get_all()
    return ppf_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_ppf_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    ppf_calculation_service = PpfCalculationService(db)
    await ppf_calculation_service.delete(uuid)

    