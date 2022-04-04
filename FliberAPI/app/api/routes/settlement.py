import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.settlement import OutSettlementSchema, SettlementSchema
from app.service.settlement import SettlementService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutSettlementSchema
)
async def create_settlement(
    order_id: str, db: AsyncSession = Depends(get_db)
) -> OutSettlementSchema:
    """ api to save settlement data. """
    settlement_service = SettlementService(db)
    settlement = await settlement_service.create(order_id)
    return settlement


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_settlement(
    payload: SettlementSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update settlement data. """
    settlement_service = SettlementService(db)
    await settlement_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutSettlementSchema
)
async def get_settlement(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutSettlementSchema:
    """ api to get settlement data. """
    settlement_service = SettlementService(db)
    settlement = await settlement_service.get_by_id(uuid)
    return settlement


@router.get("/", status_code=status.HTTP_200_OK)
async def get_settlement(db: AsyncSession = Depends(get_db)):
    """ api to get settlement data. """
    settlement_service = SettlementService(db)
    settlement = await settlement_service.get_all()
    return settlement


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_settlement(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete settlement data by id. """
    settlement_service = SettlementService(db)
    await settlement_service.delete(uuid)


@router.get("/by/order/{order_id}", status_code=status.HTTP_200_OK)
async def get_settlement(order_id: str, db: AsyncSession = Depends(get_db)):
    """ api to get settlement data buy order id. """
    settlement_service = SettlementService(db)
    settlement = await settlement_service.get_by_order_id(order_id)
    return settlement


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_settlement_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete settlement data user id. """
    settlement_service = SettlementService(db)
    await settlement_service.delete(user_id)
