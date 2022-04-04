import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.user_result import (
    OutUserResultSchema,
    InUserResultSchema,
    UserResultSchema,
)
from app.service.user_result import UserResultService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutUserResultSchema
)
async def create_user_result(
    payload: InUserResultSchema, db: AsyncSession = Depends(get_db)
) -> OutUserResultSchema:
    """ api to save user result data. """
    user_result_service = UserResultService(db)
    user_result = await user_result_service.create(payload)
    return user_result


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_user_result(
    payload: UserResultSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update user result data. """
    user_result_service = UserResultService(db)
    await user_result_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutUserResultSchema
)
async def get_user_result(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutUserResultSchema:
    """ api to get user result data by id. """
    user_result_service = UserResultService(db)
    user_result = await user_result_service.get_by_id(uuid)
    return user_result


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user_result(db: AsyncSession = Depends(get_db)):
    """ api to get user result data. """
    user_result_service = UserResultService(db)
    user_result = await user_result_service.get_all()
    return user_result


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_user_result(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user result data by id. """
    user_result_service = UserResultService(db)
    await user_result_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_user_result_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete user result data by user id. """
    user_result_service = UserResultService(db)
    await user_result_service.delete_user_result_by_user_id(user_id)
