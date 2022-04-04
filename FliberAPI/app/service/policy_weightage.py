import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.policy_weightage import PolicyWeightageRepository
from app.models.schema.policy_weightage import (
    InPolicyWeightageSchema,
    PolicyWeightageSchema,
)

logger = logging.getLogger(__name__)


class PolicyWeightageService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._policy_weightage_repository = PolicyWeightageRepository(self._db_session)

    async def create(
            self, payload: InPolicyWeightageSchema
    ):
        policy_weightage = await self._policy_weightage_repository.create(payload)
        return policy_weightage

    async def get_by_id(self, uuid: UUID):
        policy_weightage = await self._policy_weightage_repository.get_by_id(uuid)
        return policy_weightage

    async def get_all(self):
        policy_weightage = await self._policy_weightage_repository.get_all()
        return policy_weightage

    async def delete(self, uuid: UUID):
        await self._policy_weightage_repository.delete(uuid)

    async def update(self, payload: PolicyWeightageSchema):
        await self._policy_weightage_repository.update(payload)

    async def delete_policy_weightage_by_user_id(self, user_id: UUID):
        await self._policy_weightage_repository.delete_by_user_id(user_id)
