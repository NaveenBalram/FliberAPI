import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.cash_free_configuration import CashFreeConfigurationRepository
from app.models.schema.cash_free_configuration import (
    InCashFreeConfigurationSchema,
    CashFreeConfigurationSchema,
)

logger = logging.getLogger(__name__)


class CashFreeConfigurationService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._cash_free_configuration_repository = CashFreeConfigurationRepository(self._db_session)
        self.cash_free_configuration_repository = CashFreeConfigurationRepository(
            self._db_session
        )

    async def create(self, payload: InCashFreeConfigurationSchema):
        cash_free_configuration = await self.cash_free_configuration_repository.create(
            payload
        )

        return cash_free_configuration.dict()

    async def get_by_id(self, uuid: UUID):
        cash_free_configuration = (
            await self.cash_free_configuration_repository.get_by_id(uuid)
        )
        return cash_free_configuration.dict()

    async def get_all(self):
        cash_free_configuration = (
            await self.cash_free_configuration_repository.get_all()
        )
        return cash_free_configuration

    async def delete(self, uuid: UUID):
        await self.cash_free_configuration_repository.delete(uuid)

    async def update(self, payload: CashFreeConfigurationSchema):
        await self.cash_free_configuration_repository.update(payload)
