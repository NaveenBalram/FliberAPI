import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.financial_user_table import InFinancialUserTableSchema, FinancialUserTableSchema
from app.service.bonds_calculation import BondsCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_bonds_calculation(payload: InFinancialUserTableSchema, db: AsyncSession = Depends(get_db)):
    bonds_calculation_service = BondsCalculationService(db)
    bonds_calculation = await bonds_calculation_service.create(payload)
    return bonds_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bonds_calculation(payload: FinancialUserTableSchema, db: AsyncSession = Depends(get_db)):
    bonds_calculation_service = BondsCalculationService(db)
    await bonds_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_bonds_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    bonds_calculation_service = BondsCalculationService(db)
    bonds_calculation = await bonds_calculation_service.get_by_id(uuid)
    return bonds_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bonds_calculation(db: AsyncSession = Depends(get_db)):
    bonds_calculation_service = BondsCalculationService(db)
    bonds_calculation = await bonds_calculation_service.get_all()
    return bonds_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bonds_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    bonds_calculation_service = BondsCalculationService(db)
    await bonds_calculation_service.delete(uuid)
