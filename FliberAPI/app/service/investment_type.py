import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.investment_type import InvestmentTypeRepository
from app.models.schema.investment_type import (
    InInvestmentTypeSchema,
    InvestmentTypeSchema,
)

logger = logging.getLogger(__name__)


class InvestmentTypeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._investment_type_repository = InvestmentTypeRepository(self._db_session)

    async def create(self, payload: InInvestmentTypeSchema):
        investment_type = await self._investment_type_repository.create(payload)

        return investment_type

    async def get_by_id(self, uuid: UUID):
        investment_type = await self._investment_type_repository.get_by_id(uuid)
        return investment_type

    async def get_all(self):
        investment_type = await self._investment_type_repository.get_all()
        return investment_type

    async def delete(self, uuid: UUID):
        await self._investment_type_repository.delete(uuid)

    async def update(self, payload: InvestmentTypeSchema):
        await self._investment_type_repository.update(payload)

    async def delete_investment_type_by_user_id(self, user_id: UUID):
        await self._investment_type_repository.delete_by_user_id(user_id)
