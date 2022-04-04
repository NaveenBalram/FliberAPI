import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.net_worth_vehicle_data import OutNetWorthVehicleDataSchema, InNetWorthVehicleDataSchema, NetWorthVehicleDataSchemaBase, NetWorthVehicleDataSchema
from app.service.net_worth_vehicle_data import NetWorthVehicleDataService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_net_worth_vehicle_data(payload: InNetWorthVehicleDataSchema, db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_data_service = NetWorthVehicleDataService(db)
    net_worth_vehicle_data = await net_worth_vehicle_data_service.create(payload)
    return net_worth_vehicle_data


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_net_worth_vehicle_data(payload: NetWorthVehicleDataSchema, db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_data_service = NetWorthVehicleDataService(db)
    await net_worth_vehicle_data_service.update(payload)


@router.get("/{user_id}/{category_id}", status_code=status.HTTP_200_OK)
async def get_net_worth_vehicle_data(user_id: UUID, category_id: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_data_service = NetWorthVehicleDataService(db)
    net_worth_vehicle_data = await net_worth_vehicle_data_service.get_by_id(user_id, category_id)
    return net_worth_vehicle_data


@router.get("/", status_code=status.HTTP_200_OK)
async def get_net_worth_vehicle_data(db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_data_service = NetWorthVehicleDataService(db)
    net_worth_vehicle_data = await net_worth_vehicle_data_service.get_all()
    return net_worth_vehicle_data


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_net_worth_vehicle_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_data_service = NetWorthVehicleDataService(db)
    await net_worth_vehicle_data_service.delete(uuid)

