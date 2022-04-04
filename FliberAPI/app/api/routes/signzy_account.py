import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.signzy_account import (
    OutSignzyAccountSchema,
    InSignzyAccountSchema,
    SignzyAccountSchema,
)
from app.service.signzy_account import SignzyAccountService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutSignzyAccountSchema
)
async def create_signzy_account(
    payload: InSignzyAccountSchema, db: AsyncSession = Depends(get_db)
) -> OutSignzyAccountSchema:
    """ api to save signzy account data. """
    signzy_account_service = SignzyAccountService(db)
    signzy_account = await signzy_account_service.create(payload)
    return signzy_account


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_signzy_account(
    payload: SignzyAccountSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update signzy account data. """
    signzy_account_service = SignzyAccountService(db)
    await signzy_account_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutSignzyAccountSchema
)
async def get_signzy_account(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutSignzyAccountSchema:
    """ api to get signzy account data by id. """
    signzy_account_service = SignzyAccountService(db)
    signzy_account = await signzy_account_service.get_by_id(uuid)
    return signzy_account


@router.get("/", status_code=status.HTTP_200_OK)
async def get_signzy_account(db: AsyncSession = Depends(get_db)):
    """ api to get signzy account data. """
    signzy_account_service = SignzyAccountService(db)
    signzy_account = await signzy_account_service.get_all()
    return signzy_account


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_signzy_account(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete signzy account data by id. """
    signzy_account_service = SignzyAccountService(db)
    await signzy_account_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_signzy_account_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete signzy account data by user id. """
    signzy_account_service = SignzyAccountService(db)
    await signzy_account_service.delete(user_id)
