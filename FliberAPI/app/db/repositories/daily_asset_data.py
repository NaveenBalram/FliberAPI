from typing import Type

import uuid

from sqlalchemy import insert

from app.db.repositories.base import BaseRepository
from app.db.tables.daily_asset_data import DailyAssetData
from app.models.schema.daily_asset_data import (
    DailyAssetDataSchemaBase,
    DailyAssetDataSchema,
    DailyAssetDataSchema,
    InDailyAssetDataSchema,
)


class DailyAssetDataRepository(
    BaseRepository[DailyAssetDataSchemaBase, DailyAssetDataSchema, DailyAssetData]
):
    @property
    def _in_schema(self) -> Type[DailyAssetDataSchemaBase]:
        return InDailyAssetDataSchema

    @property
    def _schema(self) -> Type[DailyAssetDataSchema]:
        return DailyAssetDataSchema

    @property
    def _table(self) -> Type[DailyAssetData]:
        return DailyAssetData

    async def bulk_create(self, payload: list[DailyAssetDataSchemaBase]):
        result = []
        for data in payload:
            data = data.__dict__
            data["Id"] = uuid.uuid4()
            result.append(data)

        await self._db_session.execute(insert(self._table).values(result))
        await self._db_session.commit()
        return result
