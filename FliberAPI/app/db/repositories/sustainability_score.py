from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.sustainability_score import SustainabilityScore
from app.models.schema.sustainability_score import SustainabilityScoreSchemaBase, SustainabilityScoreSchema, SustainabilityScoreSchema, InSustainabilityScoreSchema


class SustainabilityScoreRepository(BaseRepository[SustainabilityScoreSchemaBase, SustainabilityScoreSchema, SustainabilityScore]):
    @property
    def _in_schema(self) -> Type[SustainabilityScoreSchemaBase]:
        return InSustainabilityScoreSchema

    @property
    def _schema(self) -> Type[SustainabilityScoreSchema]:
        return SustainabilityScoreSchema

    @property
    def _table(self) -> Type[SustainabilityScore]:
        return SustainabilityScore
