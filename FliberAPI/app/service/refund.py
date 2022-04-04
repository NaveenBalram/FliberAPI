import logging
from uuid import UUID, uuid4

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import CashFreeKeys
from app.db.repositories.refund import RefundRepository
from app.models.schema.refund import (
    OutRefundSchema,
    InRefundSchema,
    RefundSchema,
    RefundPayload,
)

logger = logging.getLogger(__name__)


class RefundService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._refund_repository = RefundRepository(self._db_session)

    async def create(self, refund_payload: RefundPayload):
        url = f"https://sandbox.cashfree.com/pg/orders/{refund_payload.OrderId}/refunds"
        refund_id = "refund_"
        refund_id += str(uuid4())

        payload = {
            "refund_amount": refund_payload.RefundAmount,
            "refund_id": refund_id,
            "refund_note": refund_payload.RefundNote,
        }

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        if response.status_code == 200:
            response["user_id"] = refund_payload.UserId
            payload = InRefundSchema(**response.__dict__)

            refund = await self._refund_repository.create(payload)
            return refund

        return response.json()

    async def get_by_id(self, uuid: UUID) -> OutRefundSchema:
        refund = await self._refund_repository.get_by_id(uuid)
        return refund

    async def get_all(self):
        refund = await self._refund_repository.get_all()
        return refund

    async def delete(self, uuid: UUID):
        await self._refund_repository.delete(uuid)

    async def update(self, payload: RefundSchema):
        await self._refund_repository.update(payload)

    async def get_all_refunds(self, order_id: str):
        try:
            url = f"https://sandbox.cashfree.com/pg/orders/{order_id}/refunds"

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
            else:
                result = self._refund_repository.get_by_order_id(order_id)
                if result:
                    return result
                else:
                    return response.json()

        except Exception as e:
            return str(e)

    async def get_refund(self, order_id: str, refund_id: str):
        try:
            url = (
                f"https://sandbox.cashfree.com/pg/orders/{order_id}/refunds/{refund_id}"
            )

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
            else:
                result = self._refund_repository.get_by_payment_id(order_id, refund_id)
                if result:
                    return result
                else:
                    return response.json()

        except Exception as e:
            return str(e)

    async def get_refund_by_user_id(self, user_id: UUID):
        return await self._refund_repository.get_refund(user_id)

    async def delete_refund_by_user_id(self, user_id: UUID):
        await self._refund_repository.delete_by_user_id(user_id)
