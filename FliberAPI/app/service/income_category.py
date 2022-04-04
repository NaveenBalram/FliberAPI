import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.income_category import IncomeCategoryRepository
from app.models.schema.income_category import (
    InIncomeCategorySchema,
    IncomeCategorySchema,
)

logger = logging.getLogger(__name__)


class IncomeCategoryService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._income_category_repository = IncomeCategoryRepository(self._db_session)

    async def create(self, payload: InIncomeCategorySchema):
        income_category = await self._income_category_repository.create(payload)

        return income_category

    async def get_by_id(self, uuid: UUID):
        income_category = await self._income_category_repository.get_by_id(uuid)
        return income_category

    async def get_all(self):
        income_category = await self._income_category_repository.get_all()
        return income_category

    async def delete(self, uuid: UUID):
        await self._income_category_repository.delete(uuid)

    async def update(self, payload: IncomeCategorySchema):
        await self._income_category_repository.update(payload)

    async def delete_income_category_by_user_id(self, user_id: UUID):
        await self._income_category_repository.delete_by_user_id(user_id)
