import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.expense_type import ExpenseTypeRepository
from app.models.schema.expense_type import (
    InExpenseTypeSchema,
    ExpenseTypeSchema,
)

logger = logging.getLogger(__name__)


class ExpenseTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._expense_type_repository = ExpenseTypeRepository(self._db_session)

    async def create(self, payload: InExpenseTypeSchema):
        expense_type = await self._expense_type_repository.create(payload)

        return expense_type

    async def get_by_id(self, uuid: UUID):
        expense_type = await self._expense_type_repository.get_by_id(uuid)
        return expense_type

    async def get_all(self):
        expense_type = await self._expense_type_repository.get_all()
        return expense_type

    async def delete(self, uuid: UUID):
        await self._expense_type_repository.delete(uuid)

    async def update(self, payload: ExpenseTypeSchema):
        await self._expense_type_repository.update(payload)

    async def delete_expense_type_by_user_id(self, user_id: UUID):
        await self._expense_type_repository.delete_by_user_id(user_id)
