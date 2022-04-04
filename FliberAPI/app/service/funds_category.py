import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.funds_category import FundsCategoryRepository
from app.models.schema.funds_category import (
    InFundsCategorySchema,
    FundsCategorySchema,
)

logger = logging.getLogger(__name__)


class FundsCategoryService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._funds_category_repository = FundsCategoryRepository(self._db_session)

    async def create(self, payload: InFundsCategorySchema):
        funds_category = await self._funds_category_repository.create(payload)

        return funds_category

    async def get_by_id(self, uuid: UUID):
        funds_category = await self._funds_category_repository.get_by_id(uuid)
        return funds_category

    async def get_all(self):
        funds_category = await self._funds_category_repository.get_all()
        return funds_category

    async def delete(self, uuid: UUID):
        await self._funds_category_repository.delete(uuid)

    async def update(self, payload: FundsCategorySchema):
        await self._funds_category_repository.update(payload)

    async def delete_funds_category_by_user_id(self, user_id: UUID):
        await self._funds_category_repository.delete_by_user_id(user_id)
