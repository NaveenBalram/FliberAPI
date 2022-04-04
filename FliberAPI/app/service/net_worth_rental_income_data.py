import logging

from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.net_worth_rental_income_data import NetWorthRentalIncomeDataRepository
from app.models.schema.net_worth_rental_income_data import OutNetWorthRentalIncomeDataSchema, NetWorthRentalIncomeDataSchema, InNetWorthRentalIncomeDataSchema

logger = logging.getLogger(__name__)


class NetWorthRentalIncomeDataService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._net_worth_rental_income_data_repository = NetWorthRentalIncomeDataRepository(self._db_session)

    async def create(self, payload: InNetWorthRentalIncomeDataSchema):
        net_worth_rental_income_data = await self._net_worth_rental_income_data_repository.create_and_save(payload)

        return net_worth_rental_income_data

    async def get_by_id(self, user_id: UUID, category_id: UUID):
        net_worth_rental_income_data = await self._net_worth_rental_income_data_repository.get_data(user_id, category_id)
        return net_worth_rental_income_data

    async def get_all(self):
        net_worth_rental_income_data = await self._net_worth_rental_income_data_repository.get_all_data()
        return net_worth_rental_income_data

    async def delete(self, uuid: UUID):
        await self._net_worth_rental_income_data_repository.delete(uuid)

    async def update(self, payload: NetWorthRentalIncomeDataSchema):
        await self._net_worth_rental_income_data_repository.update_data(payload)

