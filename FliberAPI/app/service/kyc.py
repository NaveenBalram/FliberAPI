import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.kyc import KycRepository
from app.models.schema.kyc import InKycSchema, KycSchema

logger = logging.getLogger(__name__)


class KycService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._kyc_repository = KycRepository(self._db_session)

    async def create(self, payload: InKycSchema):
        kyc = await self._kyc_repository.create(payload)

        return kyc

    async def get_by_id(self, uuid: UUID):
        kyc = await self._kyc_repository.get_by_id(uuid)
        return kyc

    async def get_all(self):
        kyc = await self._kyc_repository.get_all()
        return kyc

    async def delete(self, uuid: UUID):
        await self._kyc_repository.delete(uuid)

    async def update(self, payload: KycSchema):
        await self._kyc_repository.update(payload)

    async def delete_kyc_by_user_id(self, user_id: UUID):
        await self._kyc_repository.delete_by_user_id(user_id)
