import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bse_country_code import BseCountryCodeRepository
from app.models.schema.bse_country_code import (
    InBseCountryCodeSchema,
    BseCountryCodeSchema,
)

logger = logging.getLogger(__name__)


class BseCountryCodeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_country_code_repository = BseCountryCodeRepository(self._db_session)

    async def create(self, payload: InBseCountryCodeSchema):
        bse_country_code = await self._bse_country_code_repository.create(payload)

        return bse_country_code

    async def get_by_id(self, uuid: UUID):
        bse_country_code = await self._bse_country_code_repository.get_by_id(uuid)
        return bse_country_code

    async def get_all(self):
        bse_country_code = await self._bse_country_code_repository.get_all()
        return bse_country_code

    async def delete(self, uuid: UUID):
        await self._bse_country_code_repository.delete(uuid)

    async def update(self, payload: BseCountryCodeSchema):
        await self._bse_country_code_repository.update(payload)

    async def delete_bse_country_code_by_user_id(self, user_id: UUID):
        await self._bse_country_code_repository.delete_by_user_id(user_id)
