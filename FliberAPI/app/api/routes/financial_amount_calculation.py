import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.service.financial_amount_calculation import FinancialAmountCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_financial_amount_calculation(payload: InFinancialAmountCalculationSchema,
# db: AsyncSession = Depends(get_db)):
#     financial_amount_calculation_service = FinancialAmountCalculationService(db)
#     financial_amount_calculation = await financial_amount_calculation_service.create(payload)
#     return financial_amount_calculation
#
#
# @router.patch("/", status_code=status.HTTP_200_OK)
# async def update_financial_amount_calculation(payload: FinancialAmountCalculationSchema,
# db: AsyncSession = Depends(get_db)):
#     financial_amount_calculation_service = FinancialAmountCalculationService(db)
#     await financial_amount_calculation_service.update(payload)
#
#
# @router.get("/{uuid}", status_code=status.HTTP_200_OK)
# async def get_financial_amount_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     financial_amount_calculation_service = FinancialAmountCalculationService(db)
#     financial_amount_calculation = await financial_amount_calculation_service.get_by_id(uuid)
#     return financial_amount_calculation
#
#
# @router.get("/", status_code=status.HTTP_200_OK)
# async def get_financial_amount_calculation(db: AsyncSession = Depends(get_db)):
#     financial_amount_calculation_service = FinancialAmountCalculationService(db)
#     financial_amount_calculation = await financial_amount_calculation_service.get_all()
#     return financial_amount_calculation
#
#
# @router.delete("/{uuid}", status_code=status.HTTP_200_OK)
# async def delete_financial_amount_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     financial_amount_calculation_service = FinancialAmountCalculationService(db)
#     await financial_amount_calculation_service.delete(uuid)


@router.get("/total/{user_id}", status_code=status.HTTP_200_OK)
async def get_financial_amount_calculation(user_id: UUID, db: AsyncSession = Depends(get_db)):
    financial_amount_calculation_service = FinancialAmountCalculationService(db)
    financial_amount_calculation = await financial_amount_calculation_service.get_by_id(user_id)
    return financial_amount_calculation
