import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.payment_type import (
    OutPaymentTypeSchema,
    InPaymentTypeSchema,
    PaymentTypeSchema,
)
from app.service.payment_type import PaymentTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutPaymentTypeSchema
)
async def create_payment_type(
    payload: InPaymentTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutPaymentTypeSchema:
    """ api to save payment type data. """
    payment_type_service = PaymentTypeService(db)
    payment_type = await payment_type_service.create(payload)
    return payment_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_payment_type(
    payload: PaymentTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update payment type data. """
    payment_type_service = PaymentTypeService(db)
    await payment_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutPaymentTypeSchema
)
async def get_payment_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutPaymentTypeSchema:
    """ api to get payment type data by id. """
    payment_type_service = PaymentTypeService(db)
    payment_type = await payment_type_service.get_by_id(uuid)
    return payment_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_payment_type(db: AsyncSession = Depends(get_db)):
    """ api to get payment type data. """
    payment_type_service = PaymentTypeService(db)
    payment_type = await payment_type_service.get_all()
    return payment_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_payment_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete payment type data by id. """
    payment_type_service = PaymentTypeService(db)
    await payment_type_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_payment_type_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete payment type data by user id. """
    payment_type_service = PaymentTypeService(db)
    await payment_type_service.delete(user_id)
