import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.stocks_calculation import OutStocksCalculationSchema, InStocksCalculationSchema, StocksCalculationSchemaBase, StocksCalculationSchema
from app.service.stocks_calculation import StocksCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_stocks_calculation(payload: InStocksCalculationSchema, db: AsyncSession = Depends(get_db)):
    stocks_calculation_service = StocksCalculationService(db)
    stocks_calculation = await stocks_calculation_service.create(payload)
    return stocks_calculation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_stocks_calculation(payload: StocksCalculationSchema, db: AsyncSession = Depends(get_db)):
    stocks_calculation_service = StocksCalculationService(db)
    await stocks_calculation_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_stocks_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    stocks_calculation_service = StocksCalculationService(db)
    stocks_calculation = await stocks_calculation_service.get_by_id(uuid)
    return stocks_calculation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_stocks_calculation(db: AsyncSession = Depends(get_db)):
    stocks_calculation_service = StocksCalculationService(db)
    stocks_calculation = await stocks_calculation_service.get_all()
    return stocks_calculation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_stocks_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    stocks_calculation_service = StocksCalculationService(db)
    await stocks_calculation_service.delete(uuid)

    