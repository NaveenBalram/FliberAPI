import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.target_assets import TargetAssetsRepository
from app.models.schema.target_assets import (
    InTargetAssetsSchema,
    RequestTargetAssets,
    TargetAssetsSchema,
)

logger = logging.getLogger(__name__)


class TargetAssetsService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._target_assets_repository = TargetAssetsRepository(self._db_session)

    async def create(self, payload: InTargetAssetsSchema):
        target_assets = await self._target_assets_repository.create(payload)

        return target_assets

    async def get_by_id(self, uuid: UUID):
        target_assets = await self._target_assets_repository.get_by_id(uuid)
        return target_assets

    async def get_all(self):
        target_assets = await self._target_assets_repository.get_all()
        return target_assets

    async def delete(self, uuid: UUID):
        await self._target_assets_repository.delete(uuid)

    async def update(self, payload: TargetAssetsSchema):
        await self._target_assets_repository.update(payload)

    async def get_target_asset(self, payload: RequestTargetAssets):
        asset_type = ""

        if payload["age"] >= (payload["retirement"] - 5):
            asset_type = "Bronze"

        elif (
                (payload["retirement"] - 10) <= payload["age"] < (payload["retirement"] - 5)
        ):
            asset_type = "Silver"

        elif (
                (payload["retirement"] - 15)
                <= payload["age"]
                < (payload["retirement"] - 10)
        ):
            asset_type = "Gold"

        elif (payload["retirement"] - 15) > payload["age"]:
            asset_type = "Platinum"

        payload = InTargetAssetsSchema(Type=asset_type, Name=payload["type"])
        await self._target_assets_repository.get_asset(payload)

    async def delete_target_assets_by_user_id(self, user_id: UUID):
        await self._target_assets_repository.delete_by_user_id(user_id)
