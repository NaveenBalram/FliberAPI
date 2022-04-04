import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from app.db.repositories.asset_advisory import AssetAdvaisoryRepository

logger = logging.getLogger(__name__)


class AssetAdvisoryService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._asset_advisory_repository = AssetAdvaisoryRepository(self._db_session)

    async def get_advisory(self,risk_category,funding,time_to_retirement):
        asset_advisory_repository = await self._asset_advisory_repository.get_all_data(risk_category,funding,time_to_retirement)
        return asset_advisory_repository
