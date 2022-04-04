import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.role import RoleRepository
from app.models.schema.role import InRoleSchema, RoleSchema

logger = logging.getLogger(__name__)


class RoleService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._role_repository = RoleRepository(self._db_session)

    async def create(self, payload: InRoleSchema):
        role = await self._role_repository.create(payload)

        return role

    async def get_by_id(self, uuid: UUID):
        role = await self._role_repository.get_by_id(uuid)
        return role

    async def get_all(self):
        role = await self._role_repository.get_all()
        return role

    async def delete(self, uuid: UUID):
        await self._role_repository.delete(uuid)

    async def update(self, payload: RoleSchema):
        await self._role_repository.update(payload)

    async def delete_role_by_user_id(self, user_id: UUID):
        await self._role_repository.delete_by_user_id(user_id)
