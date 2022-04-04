import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_client_account import (
    OutBseClientAccountSchema,
    InBseClientAccountSchema,
    BseClientAccountSchema,
)
from app.service.bse_client_account import BseClientAccountService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_bse_client_account(
    payload: InBseClientAccountSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client account data. """
    bse_client_account_service = BseClientAccountService(db)
    bse_client_account = await bse_client_account_service.create(payload)
    return bse_client_account


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_client_account(
    payload: BseClientAccountSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse client account data. """
    bse_client_account_service = BseClientAccountService(db)
    await bse_client_account_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_bse_client_account(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse client account data id. """
    bse_client_account_service = BseClientAccountService(db)
    bse_client_account = await bse_client_account_service.get_by_id(uuid)
    return bse_client_account


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_client_account(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse client account data. """
    bse_client_account_service = BseClientAccountService(db)
    bse_client_account = await bse_client_account_service.get_all()
    return bse_client_account


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_client_account(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse client account data by id. """
    bse_client_account_service = BseClientAccountService(db)
    await bse_client_account_service.delete(uuid)


@router.delete("/by/{user_id}", status_code=status.HTTP_200_OK)
async def delete_bse_client_nominee(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse client account data by user id. """
    bse_client_nominee_service = BseClientAccountService(db)
    return await bse_client_nominee_service.delete_by_user_id(user_id)

