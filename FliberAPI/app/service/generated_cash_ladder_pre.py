import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.generated_cash_ladder_pre import (
    GeneratedCashLadderPreRepository,
)
from app.models.schema.generated_cash_ladder_pre import (
    OutGeneratedCashLadderPreSchema,
    InGeneratedCashLadderPreSchema,
    GeneratedCashLadderPreSchema,
)

logger = logging.getLogger(__name__)


class GeneratedCashLadderPreService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(self._db_session)

    async def create(
        self, payload: InGeneratedCashLadderPreSchema
    ) -> OutGeneratedCashLadderPreSchema:
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        generated_cash_ladder_pre = await self._generated_cash_ladder_pre_repository.create(
            payload
        )

        return generated_cash_ladder_pre

    async def get_by_id(self, uuid: UUID) -> OutGeneratedCashLadderPreSchema:
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        generated_cash_ladder_pre = (
            await self._generated_cash_ladder_pre_repository.get_by_id(uuid)
        )
        return generated_cash_ladder_pre

    async def get_all(self):
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        generated_cash_ladder_pre = await self._generated_cash_ladder_pre_repository.get_all()
        return generated_cash_ladder_pre

    async def delete(self, uuid: UUID):
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        await self._generated_cash_ladder_pre_repository.delete(uuid)

    async def update(self, payload: GeneratedCashLadderPreSchema):
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        await self._generated_cash_ladder_pre_repository.update(payload)

    async def bulk_create(self, payload: list):
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        await self._generated_cash_ladder_pre_repository.bulk_insert(payload)

    async def delete_generated_cash_ladder_pre_by_user_id(self, user_id: UUID):
        generated_cash_ladder_pre_repository = GeneratedCashLadderPreRepository(
            self._db_session
        )
        await self._generated_cash_ladder_pre_repository.delete_by_user_id(user_id)
