import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.funds_type import FundsTypeRepository
from app.models.schema.funds_type import (
    InFundsTypeSchema,
    FundsTypeSchema,
)

logger = logging.getLogger(__name__)


class FundsTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._funds_type_repository = FundsTypeRepository(self._db_session)

    async def create(self, payload: InFundsTypeSchema):
        funds_type = await self._funds_type_repository.create(payload)

        return funds_type

    async def get_by_id(self, uuid: UUID):
        funds_type = await self._funds_type_repository.get_by_id(uuid)
        return funds_type

    async def get_all(self):
        funds_type = await self._funds_type_repository.get_all()
        return funds_type

    async def delete(self, uuid: UUID):
        await self._funds_type_repository.delete(uuid)

    async def update(self, payload: FundsTypeSchema):
        await self._funds_type_repository.update(payload)

    async def delete_funds_type_by_user_id(self, user_id: UUID):
        await self._funds_type_repository.delete_by_user_id(user_id)
