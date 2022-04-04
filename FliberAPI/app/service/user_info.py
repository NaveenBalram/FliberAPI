import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.user_info import UserInfoRepository
from app.models.schema.user_info import (
    InUserInfoSchema,
    UserInfoSchema,
)

logger = logging.getLogger(__name__)


class UserInfoService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_info_repository = UserInfoRepository(self._db_session)

    async def create(self, payload: InUserInfoSchema):
        user_info = await self._user_info_repository.create(payload)

        return user_info

    async def get_by_id(self, uuid: UUID):
        user_info = await self._user_info_repository.get_by_id(uuid)
        return user_info

    async def get_all(self):
        user_info = await self._user_info_repository.get_all()
        return user_info

    async def delete(self, uuid: UUID):
        await self._user_info_repository.delete(uuid)

    async def update(self, payload: UserInfoSchema):
        await self._user_info_repository.update(payload)

    async def delete_user_info_by_user_id(self, user_id: UUID):
        await self._user_info_repository.delete_by_user_id(user_id)
