import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.investment_profile import InvestmentProfileRepository
from app.models.schema.investment_profile import (
    InInvestmentProfileSchema,
    InvestmentProfileSchema,
)

logger = logging.getLogger(__name__)


class InvestmentProfileService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._investment_profile_repository = InvestmentProfileRepository(self._db_session)

    async def create(
            self, payload: InInvestmentProfileSchema
    ):
        investment_profile = await self._investment_profile_repository.create(payload)

        return investment_profile

    async def get_by_id(self, uuid: UUID):
        investment_profile = await self._investment_profile_repository.get_by_id(uuid)
        return investment_profile

    async def get_all(self):
        investment_profile = await self._investment_profile_repository.get_all()
        return investment_profile

    async def delete(self, uuid: UUID):
        await self._investment_profile_repository.delete(uuid)

    async def update(self, payload: InvestmentProfileSchema):
        await self._investment_profile_repository.update(payload)

    async def delete_investment_profile_by_user_id(self, user_id: UUID):
        await self._investment_profile_repository.delete_by_user_id(user_id)
