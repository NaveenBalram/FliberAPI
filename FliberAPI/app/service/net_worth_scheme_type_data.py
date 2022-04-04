import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_scheme_type_data import NetWorthSchemeTypeDataRepository
from app.models.schema.net_worth_scheme_type_data import NetWorthSchemeTypeDataSchema, InNetWorthSchemeTypeDataSchema

logger = logging.getLogger(__name__)


class NetWorthSchemeTypeDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._net_worth_scheme_type_data_repository = NetWorthSchemeTypeDataRepository(self._db_session)

    async def create(self, payload: InNetWorthSchemeTypeDataSchema):
        net_worth_scheme_type_data = await self._net_worth_scheme_type_data_repository.create(payload)

        return net_worth_scheme_type_data

    async def get_by_id(self, uuid: UUID):
        net_worth_scheme_type_data = await self._net_worth_scheme_type_data_repository.get_by_id(uuid)
        return net_worth_scheme_type_data

    async def get_all(self):
        net_worth_scheme_type_data = await self._net_worth_scheme_type_data_repository.get_all()
        return net_worth_scheme_type_data

    async def delete(self, uuid: UUID):
        await self._net_worth_scheme_type_data_repository.delete(uuid)

    async def update(self, payload: NetWorthSchemeTypeDataSchema):
        await self._net_worth_scheme_type_data_repository.update(payload)
