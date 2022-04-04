import logging
import shutil
from uuid import UUID

from fastapi import File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import FliberUrl
from app.db.repositories.bse_client_code import BseClientCodeRepository
from app.models.schema.bse_client_code import (
    InBseClientCodeSchema,
    BseClientCodeSchema,
)
from app.models.schema.bse_client_code_screen_two import (
    BseClientCodeScreenFour,
    BseClientCodeScreenTwo,
    BseClientCodeScreenThree,
)

logger = logging.getLogger(__name__)


class BseClientCodeService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._bse_client_code_repository = BseClientCodeRepository(self._db_session)

    async def create(self, payload: InBseClientCodeSchema):
        result = await self._bse_client_code_repository.find_by_user_id(payload.UserId)

        if result is None:
            return f"User registered for the id {payload.UserId}"

        bse_client_code = await self._bse_client_code_repository.create(payload)

        return bse_client_code

    async def get_by_id(self, uuid: UUID):
        return await self._bse_client_code_repository.get_bse_user(uuid)

    async def get_all(self):
        bse_client_code = await self._bse_client_code_repository.get_all()
        return bse_client_code

    async def delete(self, uuid: UUID):
        await self._bse_client_code_repository.delete(uuid)

    async def update(self, payload: BseClientCodeSchema):
        await self._bse_client_code_repository.update(payload)

    async def update_screen_two(self, payload: BseClientCodeScreenTwo):
        await self._bse_client_code_repository.update_screen_two(payload)

    async def update_screen_three(self, payload: BseClientCodeScreenThree):
        await self._bse_client_code_repository.update_screen_three(payload)

    async def get_screen_two(self, user_id: UUID):
        return await self._bse_client_code_repository.get_screen_two(user_id)

    async def get_screen_three(self, user_id: UUID):
        return await self._bse_client_code_repository.get_screen_three(user_id)

    async def upload_file(self, user_id: UUID, image: UploadFile = File(...)):
        with open(f"images/signature/{image.filename}", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)

        image_url = f"{FliberUrl.url}/signature/{image.filename}"

        signature = BseClientCodeScreenFour(UserId=user_id, SignatureUrl=image_url)
        return await self._bse_client_code_repository.update_signature(signature)

    async def delete_bse_client_code_by_user_id(self, user_id: UUID):
        await self._bse_client_code_repository.delete_by_user_id(user_id)
