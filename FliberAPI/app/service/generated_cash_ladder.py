import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.generated_cash_ladder import GeneratedCashLadderRepository
from app.models.schema.generated_cash_ladder import (
    OutGeneratedCashLadderSchema,
    InGeneratedCashLadderSchema,
    GeneratedCashLadderSchema,
)

logger = logging.getLogger(__name__)


class GeneratedCashLadderService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._generated_cash_ladder_repository = GeneratedCashLadderRepository(self._db_session)

    async def create(
            self, payload: InGeneratedCashLadderSchema
    ):
        generated_cash_ladder = await self._generated_cash_ladder_repository.create(payload)

        return generated_cash_ladder

    async def get_by_id(self, uuid: UUID) -> OutGeneratedCashLadderSchema:
        generated_cash_ladder = await self._generated_cash_ladder_repository.get_by_id(uuid)
        return generated_cash_ladder

    async def get_all(self):
        generated_cash_ladder = await self._generated_cash_ladder_repository.get_all()
        return generated_cash_ladder

    async def delete(self, uuid: UUID):
        await self._generated_cash_ladder_repository.delete(uuid)

    async def update(self, payload: GeneratedCashLadderSchema):
        await self._generated_cash_ladder_repository.update(payload)

    async def delete_generated_cash_ladder_by_user_id(self, user_id: UUID):
        await self._generated_cash_ladder_repository.delete_by_user_id(user_id)

    async def get_by_user_id(self, user_id):
        return await self._generated_cash_ladder_repository.get_by_user_id(user_id)
