import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.user_incomes import (
    OutUserIncomesSchema,
    UserIncomesSchema,
    UserIncomesSchemaBase,
)
from app.service.user_incomes import UserIncomesService

router = APIRouter()
logger = logging.getLogger(__name__)


class UserIncomesSchemaSchema:
    """ api to  user incomes data. """
    pass


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_user_incomes(
    payload: UserIncomesSchemaBase, db: AsyncSession = Depends(get_db)
):
    """ api to save user incomes data. """
    user_incomes_service = UserIncomesService(db)
    user_incomes = await user_incomes_service.create(payload)
    return user_incomes


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_user_incomes(
    payload: UserIncomesSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update user incomes data. """
    user_incomes_service = UserIncomesService(db)
    await user_incomes_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_user_incomes(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get user incomes data by id. """
    user_incomes_service = UserIncomesService(db)
    user_incomes = await user_incomes_service.get_by_id(uuid)
    return user_incomes


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user_incomes(db: AsyncSession = Depends(get_db)):
    """ api to get user incomes data. """
    user_incomes_service = UserIncomesService(db)
    user_incomes = await user_incomes_service.get_all()
    return user_incomes


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_user_incomes(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user incomes data by id. """
    user_incomes_service = UserIncomesService(db)
    await user_incomes_service.delete(uuid)


@router.get("/by/user/id/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_incomes_by_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get user incomes data by user_id. """
    user_incomes_service = UserIncomesService(db)
    return await user_incomes_service.get_by_user_id(user_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_user_incomes_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete user incomes data by id. """
    user_incomes_service = UserIncomesService(db)
    await user_incomes_service.delete(user_id)
