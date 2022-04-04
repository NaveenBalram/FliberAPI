import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.investment_bucket import InvestmentBucketRepository
from app.models.schema.investment_bucket import (
    InInvestmentBucketSchema,
    InvestmentBucketSchema,
)

logger = logging.getLogger(__name__)


class InvestmentBucketService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._investment_bucket_repository = InvestmentBucketRepository(self._db_session)

    async def create(
            self, payload: InInvestmentBucketSchema
    ):
        investment_bucket = await self._investment_bucket_repository.create(payload)

        return investment_bucket

    async def get_by_id(self, uuid: UUID):
        investment_bucket = await self._investment_bucket_repository.get_by_id(uuid)
        return investment_bucket

    async def get_all(self):
        investment_bucket = await self._investment_bucket_repository.get_all()
        return investment_bucket

    async def delete(self, uuid: UUID):
        await self._investment_bucket_repository.delete(uuid)

    async def update(self, payload: InvestmentBucketSchema):
        await self._investment_bucket_repository.update(payload)

    async def delete_investment_bucket_by_user_id(self, user_id: UUID):
        await self._investment_bucket_repository.delete_by_user_id(user_id)
