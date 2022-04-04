import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.others_calculation import OutOthersCalculationSchema, InOthersCalculationSchema, OthersCalculationSchemaBase, OthersCalculationSchema
from app.service.others_calculation import OthersCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_others_calculation(payload: InOthersCalculationSchema, db: AsyncSession = Depends(get_db)):
    others_calculation_service = OthersCalculationService(db)
    others_calculation = await others_calculation_service.create(payload)
    return others_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_others_calculation(payload: OthersCalculationSchema, db: AsyncSession = Depends(get_db)):
    others_calculation_service = OthersCalculationService(db)
    await others_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_others_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    others_calculation_service = OthersCalculationService(db)
    others_calculation = await others_calculation_service.get_by_id(uuid)
    return others_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_others_calculation(db: AsyncSession = Depends(get_db)):
    others_calculation_service = OthersCalculationService(db)
    others_calculation = await others_calculation_service.get_all()
    return others_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_others_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    others_calculation_service = OthersCalculationService(db)
    await others_calculation_service.delete(uuid)

    