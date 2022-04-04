import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from app.db.repositories.rule_condition import RuleConditionRepository
from app.models.schema.rule_condition import (
    RuleConditionSchema,
    RuleConditionSchemaBase,
)

logger = logging.getLogger(__name__)


class RuleCondition:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def create(
            self, payload: RuleConditionSchema
    ):
        rule_condition_repository = RuleConditionRepository(self._db_session)
        rule_condition_repository = await rule_condition_repository.create(payload)

        return rule_condition_repository

    async def get_by_id(self, uuid: UUID):
        rule_condition_repository = RuleConditionRepository(self._db_session)
        rule_condition_repository = await rule_condition_repository.get_by_id(uuid)
        return rule_condition_repository

    async def get_all(self):
        rule_condition_repository = RuleConditionRepository(self._db_session)
        rule_condition_repository = await rule_condition_repository.get_all()
        return rule_condition_repository

    async def delete(self, uuid: UUID):
        rule_condition_repository = RuleConditionRepository(self._db_session)
        await rule_condition_repository.delete(uuid)

    async def update(self, payload: RuleConditionSchema):
        rule_condition_repository = RuleConditionRepository(self._db_session)
        await rule_condition_repository.update(payload)

