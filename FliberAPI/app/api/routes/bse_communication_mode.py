import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_communication_mode import (
    OutBseCommunicationModeSchema,
    InBseCommunicationModeSchema,
    BseCommunicationModeSchema,
)
from app.service.bse_communication_mode import BseCommunicationModeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_bse_communication_mode(
    payload: InBseCommunicationModeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client tax status data. """
    bse_communication_mode_service = BseCommunicationModeService(db)
    bse_communication_mode = await bse_communication_mode_service.create(payload)
    return bse_communication_mode


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_communication_mode(
    payload: BseCommunicationModeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse client tax status data. """
    bse_communication_mode_service = BseCommunicationModeService(db)
    await bse_communication_mode_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutBseCommunicationModeSchema,
)
async def get_bse_communication_mode(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse client tax status data. """
    bse_communication_mode_service = BseCommunicationModeService(db)
    bse_communication_mode = await bse_communication_mode_service.get_by_id(uuid)
    return bse_communication_mode


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_communication_mode(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse client tax status data. """
    bse_communication_mode_service = BseCommunicationModeService(db)
    bse_communication_mode = await bse_communication_mode_service.get_all()
    return bse_communication_mode


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_communication_mode(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse client tax status data by id. """
    bse_communication_mode_service = BseCommunicationModeService(db)
    return await bse_communication_mode_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_bse_communication_mode_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete bse client tax status data by user id. """
    bse_communication_mode_service = BseCommunicationModeService(db)
    return await bse_communication_mode_service.delete(user_id)

