import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_account_type import BseAccountTypeRepository
from app.models.schema.bse_account_type import (
    InBseAccountTypeSchema,
    BseAccountTypeSchema,
)

logger = logging.getLogger(__name__)


class BseAccountTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_account_type_repository = BseAccountTypeRepository(self._db_session)

    async def create(self, payload: InBseAccountTypeSchema):
        bse_account_type = await self._bse_account_type_repository.create(payload)

        return bse_account_type

    async def get_by_id(self, uuid: UUID):
        bse_account_type = await self._bse_account_type_repository.get_by_id(uuid)
        return bse_account_type

    async def get_all(self):
        bse_account_type = await self._bse_account_type_repository.get_all()
        return bse_account_type

    async def delete(self, uuid: UUID):
        await self._bse_account_type_repository.delete(uuid)

    async def update(self, payload: BseAccountTypeSchema):
        await self._bse_account_type_repository.update(payload)

    async def delete_bse_account_type_by_user_id(self, user_id: UUID):
        await self._bse_account_type_repository.delete_by_user_id(user_id)
