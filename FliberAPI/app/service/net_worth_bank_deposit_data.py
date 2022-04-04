import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_bank_deposit_data import NetWorthBankDepositDataRepository
from app.models.schema.net_worth_bank_deposit_data import NetWorthBankDepositDataSchema, InNetWorthBankDepositDataSchema

logger = logging.getLogger(__name__)


class NetWorthBankDepositDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._net_worth_bank_deposit_data_repository = NetWorthBankDepositDataRepository(self._db_session)

    async def create(self, payload: InNetWorthBankDepositDataSchema):
        net_worth_bank_deposit_data = await self._net_worth_bank_deposit_data_repository.create_and_save(payload)

        return net_worth_bank_deposit_data

    async def get_by_id(self, user_id: UUID, category_id: UUID):
        net_worth_bank_deposit_data = await self._net_worth_bank_deposit_data_repository.get_data(user_id, category_id)
        return net_worth_bank_deposit_data

    async def get_all(self):
        net_worth_bank_deposit_data = await self._net_worth_bank_deposit_data_repository.get_all_data()
        return net_worth_bank_deposit_data

    async def delete(self, uuid: UUID):
        await self._net_worth_bank_deposit_data_repository.delete(uuid)

    async def update(self, payload: NetWorthBankDepositDataSchema):
        await self._net_worth_bank_deposit_data_repository.update_data(payload)
