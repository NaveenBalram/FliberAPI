import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.income import IncomeRepository
from app.models.schema.income import InIncomeSchema, IncomeSchema

logger = logging.getLogger(__name__)


class IncomeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._income_repository = IncomeRepository(self._db_session)

    async def create(self, payload: InIncomeSchema):
        income = await self._income_repository.create(payload)

        return income

    async def get_by_id(self, uuid: UUID):
        income = await self._income_repository.get_by_id(uuid)
        return income

    async def get_all(self):
        income = await self._income_repository.get_all()
        return income

    async def delete(self, uuid: UUID):
        await self._income_repository.delete(uuid)

    async def update(self, payload: IncomeSchema):
        await self._income_repository.update(payload)

    async def delete_income_by_user_id(self, user_id: UUID):
        await self._income_repository.delete_by_user_id(user_id)
