from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.policy_weightage import PolicyWeightage
from app.models.schema.policy_weightage import (
    PolicyWeightageSchemaBase,
    PolicyWeightageSchema,
    InPolicyWeightageSchema,
)


class PolicyWeightageRepository(
    BaseRepository[PolicyWeightageSchemaBase, PolicyWeightageSchema, PolicyWeightage]
):
    @property
    def _in_schema(self) -> Type[PolicyWeightageSchemaBase]:
        return InPolicyWeightageSchema

    @property
    def _schema(self) -> Type[PolicyWeightageSchema]:
        return PolicyWeightageSchema

    @property
    def _table(self) -> Type[PolicyWeightage]:
        return PolicyWeightage
