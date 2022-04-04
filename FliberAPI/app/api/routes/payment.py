import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.payment import OutPaymentSchema, InPaymentSchema, PaymentSchema
from app.service.payment import PaymentService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutPaymentSchema)
async def create_payment(
    payload: InPaymentSchema, db: AsyncSession = Depends(get_db)
) -> OutPaymentSchema:
    """ api to save payment data. """
    payment_service = PaymentService(db)
    payment = await payment_service.create(payload)
    return payment


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_payment(payload: PaymentSchema, db: AsyncSession = Depends(get_db)):
    """ api to update payment data. """
    payment_service = PaymentService(db)
    await payment_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutPaymentSchema)
async def get_payment(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutPaymentSchema:
    """ api to get payment data by id. """
    payment_service = PaymentService(db)
    payment = await payment_service.get_by_id(uuid)
    return payment


@router.get("/", status_code=status.HTTP_200_OK)
async def get_payment(db: AsyncSession = Depends(get_db)):
    """ api to get payment data. """
    payment_service = PaymentService(db)
    payment = await payment_service.get_all()
    return payment


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_payment(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete payment data by id. """
    payment_service = PaymentService(db)
    await payment_service.delete(uuid)


@router.get("/payment/for/orders", status_code=status.HTTP_200_OK)
async def order_payment(order_id: str, db: AsyncSession = Depends(get_db)):
    """ api to get payment order data. """
    payment_service = PaymentService(db)
    return await payment_service.order_payment(order_id)


@router.get("/payment/for/orders/by/id", status_code=status.HTTP_200_OK)
async def order_payment(
    order_id: str, cf_payment_id: int, db: AsyncSession = Depends(get_db)
):
    """ api to get payment order data by id. """
    payment_service = PaymentService(db)
    return await payment_service.order_payment_by_id(order_id, cf_payment_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_payment_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete payment data by user_id. """
    payment_service = PaymentService(db)
    await payment_service.delete(user_id)
