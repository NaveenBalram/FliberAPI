import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.net_worth_calculation import OutNetWorthCalculationSchema, InNetWorthCalculationSchema, NetWorthCalculationSchemaBase, NetWorthCalculationSchema
from app.service.net_worth_calculation import NetWorthCalculationService

router = APIRouter()
logger = logging.getLogger(__name__)


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_net_worth_calculation(payload: InNetWorthCalculationSchema, db: AsyncSession = Depends(get_db)):
#     net_worth_calculation_service = NetWorthCalculationService(db)
#     net_worth_calculation = await net_worth_calculation_service.create(payload)
#     return net_worth_calculation
#
#
# @router.patch("/", status_code=status.HTTP_200_OK)
# async def update_net_worth_calculation(payload: NetWorthCalculationSchema, db: AsyncSession = Depends(get_db)):
#     net_worth_calculation_service = NetWorthCalculationService(db)
#     await net_worth_calculation_service.update(payload)


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_net_worth_calculation(user_id: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_calculation_service = NetWorthCalculationService(db)
    net_worth_calculation = await net_worth_calculation_service.get_data_by_id(user_id)
    return net_worth_calculation


# @router.get("/", status_code=status.HTTP_200_OK)
# async def get_net_worth_calculation(db: AsyncSession = Depends(get_db)):
#     net_worth_calculation_service = NetWorthCalculationService(db)
#     net_worth_calculation = await net_worth_calculation_service.get_all()
#     return net_worth_calculation
#
#
# @router.delete("/'uuid'", status_code=status.HTTP_200_OK)
# async def delete_net_worth_calculation(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     net_worth_calculation_service = NetWorthCalculationService(db)
#     await net_worth_calculation_service.delete(uuid)

    