import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bucket import OutBucketSchema, InBucketSchema, BucketSchema
from app.service.bucket import BucketService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_bucket(
    payload: InBucketSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save number of years for each bucket. """
    bucket_service = BucketService(db)
    bucket = await bucket_service.create(payload)
    return bucket


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bucket(payload: BucketSchema, db: AsyncSession = Depends(get_db)):
    """ api to update bucket data. """
    bank_account_type_service = BucketService(db)
    await bank_account_type_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutBucketSchema)
async def get_bucket_by_id(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse state data by id. """
    bank_account_type_service = BucketService(db)
    bank_account_type = await bank_account_type_service.get_by_id(uuid)
    return bank_account_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bucket_all(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse state data. """
    bank_account_type_service = BucketService(db)
    bank_account_type = await bank_account_type_service.get_all()
    return bank_account_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bucket(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse state data by id. """
    bank_account_type_service = BucketService(db)
    return await bank_account_type_service.delete(uuid)

#
# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_bucket_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
#     bucket_service = BucketService(db)
#     return await bucket_service.delete(user_id)
