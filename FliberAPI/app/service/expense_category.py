import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.expense_category import ExpenseCategoryRepository
from app.models.schema.expense_category import (
    InExpenseCategorySchema,
    ExpenseCategorySchema,
)

logger = logging.getLogger(__name__)


class ExpenseCategoryService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._expense_category_repository = ExpenseCategoryRepository(self._db_session)

    async def create(
            self, payload: InExpenseCategorySchema
    ):
        expense_category = await self._expense_category_repository.create(payload)

        return expense_category

    async def get_by_id(self, uuid: UUID):
        expense_category = await self._expense_category_repository.get_by_id(uuid)
        return expense_category

    async def get_all(self):
        expense_category = await self._expense_category_repository.get_all()
        return expense_category

    async def delete(self, uuid: UUID):
        await self._expense_category_repository.delete(uuid)

    async def update(self, payload: ExpenseCategorySchema):
        await self._expense_category_repository.update(payload)

    async def delete_expense_category_by_user_id(self, user_id: UUID):
        await self._expense_category_repository.delete_by_user_id(user_id)
