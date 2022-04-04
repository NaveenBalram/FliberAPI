import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.payment_type import PaymentTypeRepository
from app.models.schema.payment_type import (
    InPaymentTypeSchema,
    PaymentTypeSchema,
)

logger = logging.getLogger(__name__)


class PaymentTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._payment_type_repository = PaymentTypeRepository(self._db_session)

    async def create(self, payload: InPaymentTypeSchema):
        payment_type = await self._payment_type_repository.create(payload)

        return payment_type

    async def get_by_id(self, uuid: UUID):
        payment_type = await self._payment_type_repository.get_by_id(uuid)
        return payment_type

    async def get_all(self):
        payment_type = await self._payment_type_repository.get_all()
        return payment_type

    async def delete(self, uuid: UUID):
        await self._payment_type_repository.delete(uuid)

    async def update(self, payload: PaymentTypeSchema):
        await self._payment_type_repository.update(payload)

    async def delete_payment_type_by_user_id(self, user_id: UUID):
        await self._payment_type_repository.delete_by_user_id(user_id)
