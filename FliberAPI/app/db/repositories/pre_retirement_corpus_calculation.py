from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.pre_retirement_corpus_calculation import (
    PreRetirementCorpusCalculation,
)
from app.models.schema.pre_retirement_corpus_calculation import (
    PreRetirementCorpusCalculationSchemaBase,
    PreRetirementCorpusCalculationSchema,
    PreRetirementCorpusCalculationSchema,
)


class PreRetirementCorpusCalculationRepository(
    BaseRepository[
        PreRetirementCorpusCalculationSchemaBase,
        PreRetirementCorpusCalculationSchema,
        PreRetirementCorpusCalculation,
    ]
):
    @property
    def _in_schema(self) -> Type[PreRetirementCorpusCalculationSchemaBase]:
        return InPreRetirementCorpusCalculationSchema

    @property
    def _schema(self) -> Type[PreRetirementCorpusCalculationSchema]:
        return PreRetirementCorpusCalculationSchema

    @property
    def _table(self) -> Type[PreRetirementCorpusCalculation]:
        return PreRetirementCorpusCalculation
