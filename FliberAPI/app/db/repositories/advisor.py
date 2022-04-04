from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.advisor import Advisor
from app.models.schema.advisor import InAdvisorSchema, AdvisorSchema


class AdvisorRepository(BaseRepository[InAdvisorSchema, AdvisorSchema, Advisor]):
    @property
    def _in_schema(self) -> Type[InAdvisorSchema]:
        return InAdvisorSchema

    @property
    def _schema(self) -> Type[AdvisorSchema]:
        return AdvisorSchema

    @property
    def _table(self) -> Type[Advisor]:
        return Advisor
