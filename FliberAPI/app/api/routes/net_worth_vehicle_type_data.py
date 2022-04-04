import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.net_worth_vehicle_type_data import InNetWorthVehicleTypeDataSchema, NetWorthVehicleTypeDataSchema
from app.service.net_worth_vehicle_type_data import NetWorthVehicleTypeDataService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_net_worth_vehicle_type_data(payload: InNetWorthVehicleTypeDataSchema,
                                             db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_type_data_service = NetWorthVehicleTypeDataService(db)
    net_worth_vehicle_type_data = await net_worth_vehicle_type_data_service.create(payload)
    return net_worth_vehicle_type_data


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_net_worth_vehicle_type_data(payload: NetWorthVehicleTypeDataSchema,
                                             db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_type_data_service = NetWorthVehicleTypeDataService(db)
    await net_worth_vehicle_type_data_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_net_worth_vehicle_type_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_type_data_service = NetWorthVehicleTypeDataService(db)
    net_worth_vehicle_type_data = await net_worth_vehicle_type_data_service.get_by_id(uuid)
    return net_worth_vehicle_type_data


@router.get("/", status_code=status.HTTP_200_OK)
async def get_net_worth_vehicle_type_data(db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_type_data_service = NetWorthVehicleTypeDataService(db)
    net_worth_vehicle_type_data = await net_worth_vehicle_type_data_service.get_all()
    return net_worth_vehicle_type_data


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_net_worth_vehicle_type_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_vehicle_type_data_service = NetWorthVehicleTypeDataService(db)
    await net_worth_vehicle_type_data_service.delete(uuid)
