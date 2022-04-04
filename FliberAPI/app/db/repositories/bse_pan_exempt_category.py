from typing import Type

from app.db.repositories.base import BaseRepository
from app.db.tables.bse_pan_exempt_category import BsePanExemptCategory
from app.models.schema.bse_pan_exempt_category import (
    BsePanExemptCategorySchemaBase,
    BsePanExemptCategorySchema,
    InBsePanExemptCategorySchema,
)


class BsePanExemptCategoryRepository(
    BaseRepository[
        BsePanExemptCategorySchemaBase, BsePanExemptCategorySchema, BsePanExemptCategory
    ]
):
    @property
    def _in_schema(self) -> Type[BsePanExemptCategorySchemaBase]:
        return InBsePanExemptCategorySchema

    @property
    def _schema(self) -> Type[BsePanExemptCategorySchema]:
        return BsePanExemptCategorySchema

    @property
    def _table(self) -> Type[BsePanExemptCategory]:
        return BsePanExemptCategory
