import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_user_table_data import NetWorthUserTableDataRepository
from app.models.schema.net_worth_user_table_data import NetWorthUserTableDataSchema, InNetWorthUserTableDataSchema

logger = logging.getLogger(__name__)


class NetWorthUserTableDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

        self._net_worth_user_table_data_repository = NetWorthUserTableDataRepository(self._db_session)

    async def create(self, payload: InNetWorthUserTableDataSchema):
        net_worth_user_table_data = await self._net_worth_user_table_data_repository.create(payload)

        return net_worth_user_table_data

    async def get_by_id(self, uuid: UUID):
        net_worth_user_table_data = await self._net_worth_user_table_data_repository.get_by_id(uuid)
        return net_worth_user_table_data

    async def get_all(self):
        net_worth_user_table_data = await self._net_worth_user_table_data_repository.get_all()
        return net_worth_user_table_data

    async def delete(self, uuid: UUID):
        await self._net_worth_user_table_data_repository.delete(uuid)

    async def update(self, payload: NetWorthUserTableDataSchema):
        await self._net_worth_user_table_data_repository.update(payload)
