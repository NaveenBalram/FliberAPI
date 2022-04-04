from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.rule_condition import RuleCondition
from app.models.schema.rule_condition import RuleConditionSchema,RuleConditionSchemaBase


class RuleConditionRepository(BaseRepository[RuleConditionSchema,RuleConditionSchemaBase,RuleCondition]):
    @property
    def _in_schema(self) -> Type[RuleConditionSchema]:
        return RuleConditionSchema

    @property
    def _schema(self) -> Type[RuleConditionSchemaBase]:
        return RuleConditionSchemaBase

    @property
    def _table(self) -> Type[RuleCondition]:
        return RuleCondition