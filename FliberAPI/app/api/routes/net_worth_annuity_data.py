import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.net_worth_annuity_data import InNetWorthAnnuityDataSchema, NetWorthAnnuityDataSchema
from app.service.net_worth_annuity_data import NetWorthAnnuityDataService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_net_worth_annuity_data(payload: InNetWorthAnnuityDataSchema, db: AsyncSession = Depends(get_db)):
    net_worth_annuity_data_service = NetWorthAnnuityDataService(db)
    net_worth_annuity_data = await net_worth_annuity_data_service.create(payload)
    return net_worth_annuity_data


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_net_worth_annuity_data(payload: NetWorthAnnuityDataSchema, db: AsyncSession = Depends(get_db)):
    net_worth_annuity_data_service = NetWorthAnnuityDataService(db)
    await net_worth_annuity_data_service.update(payload)


@router.get("/{user_id}/{category_id}", status_code=status.HTTP_200_OK)
async def get_net_worth_annuity_data(user_id: UUID, category_id: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_annuity_data_service = NetWorthAnnuityDataService(db)
    net_worth_annuity_data = await net_worth_annuity_data_service.get_by_id(user_id, category_id)
    return net_worth_annuity_data


@router.get("/", status_code=status.HTTP_200_OK)
async def get_net_worth_annuity_data(db: AsyncSession = Depends(get_db)):
    net_worth_annuity_data_service = NetWorthAnnuityDataService(db)
    net_worth_annuity_data = await net_worth_annuity_data_service.get_all()
    return net_worth_annuity_data


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_net_worth_annuity_data(uuid: UUID, db: AsyncSession = Depends(get_db)):
    net_worth_annuity_data_service = NetWorthAnnuityDataService(db)
    await net_worth_annuity_data_service.delete(uuid)
