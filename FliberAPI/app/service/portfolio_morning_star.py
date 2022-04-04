import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.portfolio_morning_star import PortfolioMorningStarRepository
from app.models.schema.portfolio_morning_star import (
    InPortfolioMorningStarSchema,
    PortfolioMorningStarSchema,
)

logger = logging.getLogger(__name__)


class PortfolioMorningStarService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._portfolio_morning_star_repository = PortfolioMorningStarRepository(self._db_session)

    async def create(
            self, payload: InPortfolioMorningStarSchema
    ):
        portfolio_morning_star = await self._portfolio_morning_star_repository.create(payload)
        return portfolio_morning_star

    async def get_by_id(self, uuid: UUID):
        portfolio_morning_star = await self._portfolio_morning_star_repository.get_by_id(uuid)
        return portfolio_morning_star

    async def get_all(self):
        portfolio_morning_star = await self._portfolio_morning_star_repository.get_all()
        return portfolio_morning_star

    async def delete(self, uuid: UUID):
        await self._portfolio_morning_star_repository.delete(uuid)

    async def update(self, payload: PortfolioMorningStarSchema):
        await self._portfolio_morning_star_repository.update(payload)

    async def delete_portfolio_morning_star_by_user_id(self, user_id: UUID):
        await self._portfolio_morning_star_repository.delete_by_user_id(user_id)
