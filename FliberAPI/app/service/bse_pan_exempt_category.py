import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_pan_exempt_category import BsePanExemptCategoryRepository
from app.models.schema.bse_pan_exempt_category import (
    OutBsePanExemptCategorySchema,
    InBsePanExemptCategorySchema,
    BsePanExemptCategorySchema,
)

logger = logging.getLogger(__name__)


class BsePanExemptCategoryService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_pan_exempt_category_repository = BsePanExemptCategoryRepository(self._db_session)

    async def create(
            self, payload: InBsePanExemptCategorySchema
    ):
        bse_pan_exempt_category = await self._bse_pan_exempt_category_repository.create(
            payload
        )

        return bse_pan_exempt_category

    async def get_by_id(self, uuid: UUID) -> OutBsePanExemptCategorySchema:
        bse_pan_exempt_category = await self._bse_pan_exempt_category_repository.get_by_id(
            uuid
        )
        return bse_pan_exempt_category

    async def get_all(self):
        bse_pan_exempt_category = await self._bse_pan_exempt_category_repository.get_all()
        return bse_pan_exempt_category

    async def delete(self, uuid: UUID):
        await self._bse_pan_exempt_category_repository.delete(uuid)

    async def update(self, payload: BsePanExemptCategorySchema):
        await self._bse_pan_exempt_category_repository.update(payload)

    async def delete_bse_pan_exempt_category_by_user_id(self, user_id: UUID):
        await self._bse_pan_exempt_category_repository.delete_by_user_id(user_id)
