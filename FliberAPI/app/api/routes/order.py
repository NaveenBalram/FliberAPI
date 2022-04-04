import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.order import (
    OutOrderSchema,
    InOrderSchema,
    OrderSchemaBase,
    RequestOrderSchema,
    OrderSchema,
    RequestOrderPayment,
)
from app.service.order import OrderService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutOrderSchema)
async def create_order(
    payload: InOrderSchema, db: AsyncSession = Depends(get_db)
) -> OutOrderSchema:
    """ api to save order data. """
    order_service = OrderService(db)
    order = await order_service.create(payload)
    return order


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_order(payload: OrderSchema, db: AsyncSession = Depends(get_db)):
    """ api to update order data. """
    order_service = OrderService(db)
    await order_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutOrderSchema)
async def get_order(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutOrderSchema:
    """ api to get order data by id. """
    order_service = OrderService(db)
    order = await order_service.get_by_id(uuid)
    return order


@router.get("/", status_code=status.HTTP_200_OK)
async def get_order(db: AsyncSession = Depends(get_db)):
    """ api to get order data. """
    order_service = OrderService(db)
    order = await order_service.get_all()
    return order


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_order(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete order data by id. """
    order_service = OrderService(db)
    await order_service.delete(uuid)


@router.post("/generate", status_code=status.HTTP_200_OK)
async def generate_order(
    payload: RequestOrderSchema, db: AsyncSession = Depends(get_db)
) -> OutOrderSchema:
    """ api to generate order data. """
    order_service = OrderService(db)
    order = await order_service.create_order(payload)
    return order


@router.post("/pay", status_code=status.HTTP_200_OK)
async def pay_order(
    payload: RequestOrderPayment, db: AsyncSession = Depends(get_db)
) -> OutOrderSchema:
    """ api to save pay order data. """
    order_service = OrderService(db)
    order = await order_service.order_pay(payload)
    return order


@router.get("/pay/{order_id}", status_code=status.HTTP_200_OK)
async def pay_order(
    order_id: str, db: AsyncSession = Depends(get_db)
) -> OutOrderSchema:
    """ api to fetch order data. """
    order_service = OrderService(db)
    order = await order_service.get_order_data_from_cashfree(order_id)
    return order


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_order_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete order data by user_id. """
    order_service = OrderService(db)
    await order_service.delete(user_id)
