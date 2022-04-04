import logging
from uuid import UUID

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import CashFreeKeys
from app.db.repositories.settlement import SettlementRepository
from app.models.schema.settlement import (
    SettlementSchema,
)

logger = logging.getLogger(__name__)


class SettlementService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._settlement_repository = SettlementRepository(self._db_session)

    async def create(self, order_id: str):
        url = f"https://sandbox.cashfree.com/pg/orders/{order_id}/settlements"

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }

        response = requests.request("GET", url, headers=headers).json()

        payload = response
        settlement = await self._settlement_repository.create(payload)

        return settlement

    async def get_by_id(self, uuid: UUID):
        settlement = await self._settlement_repository.get_by_id(uuid)
        return settlement

    async def get_all(self):
        settlement = await self._settlement_repository.get_all()
        return settlement

    async def delete(self, uuid: UUID):
        await self._settlement_repository.delete(uuid)

    async def update(self, payload: SettlementSchema):
        await self._settlement_repository.update(payload)

    async def get_by_order_id(self, order_id: str):
        url = f"https://sandbox.cashfree.com/pg/orders/{order_id}/settlements"

        headers = {
            "Accept": "application/json",
            "x-api-version": "2021-05-21",
            "Content-Type": "application/json",
            "x-client-id": CashFreeKeys.KEY_ID,
            "x-client-secret": CashFreeKeys.KEY_SECRET,
        }

        return requests.request("GET", url, headers=headers).json()

    async def delete_settlement_by_user_id(self, user_id: UUID):
        await self._settlement_repository.delete_by_user_id(user_id)
