import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_income_slab import BSEIncomeSlabRepository
from app.models.schema.bse_income_slab import (
    InBSEIncomeSlabSchema,
    BSEIncomeSlabSchema,
)

logger = logging.getLogger(__name__)


class BSEIncomeSlabService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_income_slab_repository = BSEIncomeSlabRepository(self._db_session)

    async def create(self, payload: InBSEIncomeSlabSchema):
        bse_income_slab = await self._bse_income_slab_repository.create(payload)
        return bse_income_slab

    async def get_by_id(self, uuid: UUID):
        bse_income_slab = await self._bse_income_slab_repository.get_by_id(uuid)
        return bse_income_slab

    async def get_all(self):
        bse_income_slab = await self._bse_income_slab_repository.get_all()
        return bse_income_slab

    async def delete(self, uuid: UUID):
        await self._bse_income_slab_repository.delete(uuid)

    async def update(self, payload: BSEIncomeSlabSchema):
        await self._bse_income_slab_repository.update(payload)

    async def delete_bse_income_slab_by_user_id(self, user_id: UUID):
        await self._bse_income_slab_repository.delete_by_user_id(user_id)
