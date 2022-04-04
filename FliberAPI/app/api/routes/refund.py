import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.refund import OutRefundSchema, RefundSchema, RefundPayload
from app.service.refund import RefundService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutRefundSchema)
async def create_refund(
    payload: RefundPayload, db: AsyncSession = Depends(get_db)
) -> OutRefundSchema:
    """ api to save refund data. """
    refund_service = RefundService(db)
    refund = await refund_service.create(payload)
    return refund


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_refund(payload: RefundSchema, db: AsyncSession = Depends(get_db)):
    """ api to update refund data. """
    refund_service = RefundService(db)
    await refund_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutRefundSchema)
async def get_refund(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutRefundSchema:
    """ api to get refund data by id. """
    refund_service = RefundService(db)
    refund = await refund_service.get_by_id(uuid)
    return refund


@router.get("/", status_code=status.HTTP_200_OK)
async def get_refund(db: AsyncSession = Depends(get_db)):
    """ api to get refund data. """
    refund_service = RefundService(db)
    refund = await refund_service.get_all()
    return refund


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_refund(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete refund data by id. """
    refund_service = RefundService(db)
    await refund_service.delete(uuid)


@router.get("/all/by/order/{order_id}", status_code=status.HTTP_200_OK)
async def get_all_refund_by_order_id(order_id: str, db: AsyncSession = Depends(get_db)):
    """ api to get order data by order id. """
    refund_service = RefundService(db)
    return await refund_service.get_all_refunds(order_id)


@router.get("/all/by/order/{order_id}", status_code=status.HTTP_200_OK)
async def get_by_refund_id_order_id(
    order_id: str, refund_id: str, db: AsyncSession = Depends(get_db)
):
    """ api to get refund data by refund id and order id. """
    refund_service = RefundService(db)
    return await refund_service.get_refund(order_id, refund_id)


@router.get("/all/by/order/{user_id}", status_code=status.HTTP_200_OK)
async def get_refund_bu_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get refund data by user id. """
    refund_service = RefundService(db)
    return await refund_service.get_refund_by_user_id(user_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_refund_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete refund data by user_id. """
    refund_service = RefundService(db)
    await refund_service.delete_refund_by_user_id(user_id)
