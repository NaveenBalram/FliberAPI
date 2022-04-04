import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.generated_incomes import GeneratedIncomesRepository
from app.models.schema.generated_incomes import (
    InGeneratedIncomesSchema,
    GeneratedIncomesSchema,
)

logger = logging.getLogger(__name__)


class GeneratedIncomesService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._generated_incomes_repository = GeneratedIncomesRepository(self._db_session)

    async def create(
            self, payload: InGeneratedIncomesSchema
    ):
        generated_incomes = await self._generated_incomes_repository.create(payload)

        return generated_incomes

    async def get_by_id(self, uuid: UUID):
        generated_incomes = await self._generated_incomes_repository.get_by_id(uuid)
        return generated_incomes

    async def get_all(self):
        generated_incomes = await self._generated_incomes_repository.get_all()
        return generated_incomes

    async def delete(self, uuid: UUID):
        await self._generated_incomes_repository.delete(uuid)

    async def update(self, payload: GeneratedIncomesSchema):
        await self._generated_incomes_repository.update(payload)

    async def delete_generated_incomes_by_user_id(self, user_id: UUID):
        await self._generated_incomes_repository.delete_by_user_id(user_id)
