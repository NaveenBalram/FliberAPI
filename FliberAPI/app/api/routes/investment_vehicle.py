import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.investment_vehicle import (
    OutInvestmentVehicleSchema,
    InInvestmentVehicleSchema,
    InvestmentVehicleSchema,
)
from app.service.investment_vehicle import InvestmentVehicleService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutInvestmentVehicleSchema
)
async def create_investment_vehicle(
    payload: InInvestmentVehicleSchema, db: AsyncSession = Depends(get_db)
) -> OutInvestmentVehicleSchema:
    investment_vehicle_service = InvestmentVehicleService(db)
    investment_vehicle = await investment_vehicle_service.create(payload)
    return investment_vehicle


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_investment_vehicle(
    payload: InvestmentVehicleSchema, db: AsyncSession = Depends(get_db)
):
    investment_vehicle_service = InvestmentVehicleService(db)
    await investment_vehicle_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutInvestmentVehicleSchema
)
async def get_investment_vehicle(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutInvestmentVehicleSchema:
    investment_vehicle_service = InvestmentVehicleService(db)
    investment_vehicle = await investment_vehicle_service.get_by_id(uuid)
    return investment_vehicle


@router.get("/", status_code=status.HTTP_200_OK)
async def get_investment_vehicle(db: AsyncSession = Depends(get_db)):
    investment_vehicle_service = InvestmentVehicleService(db)
    investment_vehicle = await investment_vehicle_service.get_all()
    return investment_vehicle


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_investment_vehicle(uuid: UUID, db: AsyncSession = Depends(get_db)):
    investment_vehicle_service = InvestmentVehicleService(db)
    await investment_vehicle_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_investment_vehicle_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    investment_vehicle_service = InvestmentVehicleService(db)
    await investment_vehicle_service.delete(user_id)
