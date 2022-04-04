import logging
from uuid import UUID

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import CashFreeKeys
from app.db.repositories.payment import PaymentRepository
from app.models.schema.payment import (
    InPaymentSchema,
    PaymentSchema,
    PaymentSchemaBase,
)

logger = logging.getLogger(__name__)


class PaymentService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._payment_repository = PaymentRepository(self._db_session)

    async def create(self, payload: InPaymentSchema):
        payment = await self._payment_repository.create(payload)

        return payment

    async def get_by_id(self, uuid: UUID):
        payment = await self._payment_repository.get_by_id(uuid)
        return payment

    async def get_all(self):
        payment = await self._payment_repository.get_all()
        return payment

    async def delete(self, uuid: UUID):
        await self._payment_repository.delete(uuid)

    async def update(self, payload: PaymentSchema):
        await self._payment_repository.update(payload)

    async def order_payment(self, order_id: str):
        url = f"https://sandbox.cashfree.com/pg/orders/{order_id}/payments"

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }
        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            payload = PaymentSchemaBase(**response.json())
            await self._payment_repository.create(payload)
        return response.json()

    async def order_payment_by_id(self, order_id: str, cf_payment_id: int):

        url = f"https://sandbox.cashfree.com/pg/orders/{order_id}/payments/{cf_payment_id}"

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            return response.json()

        result = self._payment_repository.get_by_payment_id(
            payment_id=cf_payment_id, order_id=order_id
        )
        if result:
            return result
        else:
            return response.json()

    async def delete_payment_by_user_id(self, user_id: UUID):
        await self._payment_repository.delete_by_user_id(user_id)
