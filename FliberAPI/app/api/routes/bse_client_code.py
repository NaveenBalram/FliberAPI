import logging
from uuid import UUID

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_client_code import InBseClientCodeSchema, BseClientCodeSchema
from app.models.schema.bse_client_code_screen_two import (
    BseClientCodeScreenTwo,
    BseClientCodeScreenThree,
)
from app.service.bse_client_code import BseClientCodeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_bse_client_code(
    payload: InBseClientCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client code data. """
    bse_user_account_service = BseClientCodeService(db)
    bse_user_account = await bse_user_account_service.create(payload)
    return bse_user_account


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_user_account(
    payload: BseClientCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse client code data. """
    bse_user_account_service = BseClientCodeService(db)
    await bse_user_account_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK)
async def get_bse_user_account(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch bse client code data by id. """
    bse_user_account_service = BseClientCodeService(db)
    bse_user_account = await bse_user_account_service.get_by_id(uuid)
    return bse_user_account


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_user_account(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse client code data. """
    bse_user_account_service = BseClientCodeService(db)
    bse_user_account = await bse_user_account_service.get_all()
    return bse_user_account


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_user_account(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse client code data by id. """
    bse_user_account_service = BseClientCodeService(db)
    await bse_user_account_service.delete(uuid)


@router.post("/upload/signature")
async def create_upload_file(
    user_id: UUID, image: UploadFile = File(...), db: AsyncSession = Depends(get_db)
):
    """ api to upload signature. """
    bse_user_account_service = BseClientCodeService(db)
    return await bse_user_account_service.upload_file(user_id, image)


@router.get("/screen/two/{user_id}", status_code=status.HTTP_200_OK)
async def get_screen_two_data(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch second screen data by user id. """
    bse_user_account_service = BseClientCodeService(db)
    return await bse_user_account_service.get_screen_two(user_id)


@router.get("/screen/three/{user_id}", status_code=status.HTTP_200_OK)
async def get_screen_three_data(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch third screen data. """
    bse_user_account_service = BseClientCodeService(db)
    return await bse_user_account_service.get_screen_three(user_id)


@router.patch("/screen/two/{user_id}", status_code=status.HTTP_200_OK)
async def update_screen_two_data(
    payload: BseClientCodeScreenTwo, db: AsyncSession = Depends(get_db)
):
    """ api to update second screen data. """
    bse_user_account_service = BseClientCodeService(db)
    await bse_user_account_service.update_screen_two(payload)


@router.patch("/screen/three/{user_id}", status_code=status.HTTP_200_OK)
async def update_screen_three_data(
    payload: BseClientCodeScreenThree, db: AsyncSession = Depends(get_db)
):
    """ api to update third screen data. """
    bse_user_account_service = BseClientCodeService(db)
    return await bse_user_account_service.update_screen_three(payload)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_bse_client_code_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete bse client code data. """
    bse_client_code_service = BseClientCodeService(db)
    return await bse_client_code_service.delete(user_id)
