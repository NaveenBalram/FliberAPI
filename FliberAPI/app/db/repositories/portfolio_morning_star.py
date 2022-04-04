from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.portfolio_morning_star import PortfolioMorningStar
from app.models.schema.portfolio_morning_star import (
    PortfolioMorningStarSchemaBase,
    PortfolioMorningStarSchema,
    InPortfolioMorningStarSchema,
)


class PortfolioMorningStarRepository(
    BaseRepository[
        PortfolioMorningStarSchemaBase, PortfolioMorningStarSchema, PortfolioMorningStar
    ]
):
    @property
    def _in_schema(self) -> Type[PortfolioMorningStarSchemaBase]:
        return InPortfolioMorningStarSchema

    @property
    def _schema(self) -> Type[PortfolioMorningStarSchema]:
        return PortfolioMorningStarSchema

    @property
    def _table(self) -> Type[PortfolioMorningStar]:
        return PortfolioMorningStar
