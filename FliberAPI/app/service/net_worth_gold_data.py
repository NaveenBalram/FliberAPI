import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_gold_data import NetWorthGoldDataRepository
from app.models.schema.net_worth_gold_data import NetWorthGoldDataSchema, InNetWorthGoldDataSchema

logger = logging.getLogger(__name__)


class NetWorthGoldDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._net_worth_gold_data_repository = NetWorthGoldDataRepository(self._db_session)

    async def create(self, payload: InNetWorthGoldDataSchema):
        net_worth_gold_data = await self._net_worth_gold_data_repository.create_and_save(payload)
        return net_worth_gold_data

    async def get_by_id(self, user_id: UUID, category_id: UUID):
        net_worth_gold_data = await self._net_worth_gold_data_repository.get_data(user_id, category_id)
        return net_worth_gold_data

    async def get_all(self):
        net_worth_gold_data = await self._net_worth_gold_data_repository.get_all_data()
        return net_worth_gold_data

    async def delete(self, uuid: UUID):
        await self._net_worth_gold_data_repository.delete_by_user_id(uuid)

    async def update(self, payload: NetWorthGoldDataSchema):
        await self._net_worth_gold_data_repository.update_data(payload)
