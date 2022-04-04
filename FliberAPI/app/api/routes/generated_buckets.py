import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.generated_buckets import (
    InGeneratedBucketsSchema,
    GeneratedBucketsSchema,
)
from app.service.generated_buckets import GeneratedBucketsService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_generated_buckets(
        payload: InGeneratedBucketsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save generated bucket for post retirement and pre retirement data. """
    generated_buckets_service = GeneratedBucketsService(db)
    generated_buckets = await generated_buckets_service.create(payload)
    return generated_buckets


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_generated_buckets(
        payload: GeneratedBucketsSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update generated bucket."""
    generated_buckets_service = GeneratedBucketsService(db)
    await generated_buckets_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_generated_buckets(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch generated bucket by id. """
    generated_buckets_service = GeneratedBucketsService(db)
    generated_buckets = await generated_buckets_service.get_by_id(uuid)
    return generated_buckets


@router.get("/by/{user_id}", status_code=status.HTTP_200_OK)
async def get_generated_buckets_by_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to fetch generated bucket by user id. """
    generated_buckets_service = GeneratedBucketsService(db)
    generated_buckets = await generated_buckets_service.get_by_user_id(user_id)
    return generated_buckets


@router.get("/", status_code=status.HTTP_200_OK)
async def get_generated_buckets(db: AsyncSession = Depends(get_db)):
    """ api to fetch all generated bucket. """
    generated_buckets_service = GeneratedBucketsService(db)
    generated_buckets = await generated_buckets_service.get_all()
    return generated_buckets


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_generated_buckets(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete generated bucket by id. """
    generated_buckets_service = GeneratedBucketsService(db)
    await generated_buckets_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_generated_buckets_by_user_id(
        user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete generated bucket by user id. """
    generated_buckets_service = GeneratedBucketsService(db)
    await generated_buckets_service.delete(user_id)
