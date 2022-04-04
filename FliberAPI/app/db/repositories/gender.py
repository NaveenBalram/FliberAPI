from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.gender import Gender
from app.models.schema.gender import InGenderSchema, GenderSchema


class GenderRepository(BaseRepository[InGenderSchema, GenderSchema, Gender]):
    @property
    def _in_schema(self) -> Type[InGenderSchema]:
        return InGenderSchema

    @property
    def _schema(self) -> Type[GenderSchema]:
        return GenderSchema

    @property
    def _table(self) -> Type[Gender]:
        return Gender
