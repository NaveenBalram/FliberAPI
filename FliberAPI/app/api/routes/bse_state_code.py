import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_state_code import (
    OutBseStateCodeSchema,
    InBseStateCodeSchema,
    BseStateCodeSchema,
)
from app.service.bse_state_code import BseStateCodeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_bse_state_code(
    payload: InBseStateCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse state data. """
    bse_state_code_service = BseStateCodeService(db)
    bse_state_code = await bse_state_code_service.create(payload)
    return bse_state_code


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_state_code(
    payload: BseStateCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse state data. """
    bse_state_code_service = BseStateCodeService(db)
    await bse_state_code_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_bse_state_code(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse state data by id. """
    bse_state_code_service = BseStateCodeService(db)
    bse_state_code = await bse_state_code_service.get_by_id(uuid)
    return bse_state_code


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_state_code(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse state data. """
    bse_state_code_service = BseStateCodeService(db)
    bse_state_code = await bse_state_code_service.get_all()
    return bse_state_code


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_state_code(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse state data by id. """
    bse_state_code_service = BseStateCodeService(db)
    await bse_state_code_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_bse_state_code_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete bse state data by user id. """
    bse_state_code_service = BseStateCodeService(db)
    return bse_state_code_service.delete(user_id)
