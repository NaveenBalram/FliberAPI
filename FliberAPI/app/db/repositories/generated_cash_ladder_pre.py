from typing import Type

import uuid

from sqlalchemy import insert
from sqlalchemy.orm.session import Session

from app.db.repositories.base import BaseRepository
from app.db.tables.generated_cash_ladder_pre import GeneratedCashLadderPre
from app.models.schema.generated_cash_ladder_pre import (
    GeneratedCashLadderPreSchemaBase,
    GeneratedCashLadderPreSchema,
    InGeneratedCashLadderPreSchema,
)


class GeneratedCashLadderPreRepository(
    BaseRepository[
        GeneratedCashLadderPreSchemaBase,
        GeneratedCashLadderPreSchema,
        GeneratedCashLadderPre,
    ]
):
    @property
    def _in_schema(self) -> Type[GeneratedCashLadderPreSchemaBase]:
        return InGeneratedCashLadderPreSchema

    @property
    def _schema(self) -> Type[GeneratedCashLadderPreSchema]:
        return GeneratedCashLadderPreSchema

    @property
    def _table(self) -> Type[GeneratedCashLadderPre]:
        return GeneratedCashLadderPre

    async def bulk_insert(self, payload: list[GeneratedCashLadderPreSchemaBase]):
        result = []
        for data in payload:
            data = data.__dict__
            data["Id"] = uuid.uuid4()
            result.append(data)

        await self._db_session.execute(insert(self._table).values(result))
        await self._db_session.commit()
        return result
