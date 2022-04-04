import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.income_type import IncomeTypeRepository
from app.models.schema.income_type import (
    InIncomeTypeSchema,
    IncomeTypeSchema,
)

logger = logging.getLogger(__name__)


class IncomeTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._income_type_repository = IncomeTypeRepository(self._db_session)

    async def create(self, payload: InIncomeTypeSchema):
        income_type = await self._income_type_repository.create(payload)

        return income_type

    async def get_by_id(self, uuid: UUID):
        income_type = await self._income_type_repository.get_by_id(uuid)
        return income_type

    async def get_all(self):
        income_type = await self._income_type_repository.get_all()
        return income_type

    async def delete(self, uuid: UUID):
        await self._income_type_repository.delete(uuid)

    async def update(self, payload: IncomeTypeSchema):
        await self._income_type_repository.update(payload)

    async def delete_income_type_by_user_id(self, user_id: UUID):
        await self._income_type_repository.delete_by_user_id(user_id)
