import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.gender import OutGenderSchema, InGenderSchema, GenderSchema
from app.service.gender import GenderService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_gender(
    payload: InGenderSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save gender data. """
    gender_service = GenderService(db)
    gender = await gender_service.create(payload)
    return gender


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_gender(payload: GenderSchema, db: AsyncSession = Depends(get_db)):
    """ api to update gender data. """
    gender_service = GenderService(db)
    await gender_service.update(payload)


@router.get(
    "/{gender_id}", status_code=status.HTTP_200_OK
)
async def get_gender(
    gender_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch gender data by id. """
    gender_service = GenderService(db)
    gender = await gender_service.get_by_id(gender_id)
    return gender


@router.get("/", status_code=status.HTTP_200_OK)
async def get_gender(db: AsyncSession = Depends(get_db)):
    """ api fetch all gender data. """
    gender_service = GenderService(db)
    gender = await gender_service.get_all()
    return gender


@router.delete("/{gender_id}", status_code=status.HTTP_200_OK)
async def delete_gender(gender_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete gender data by id. """
    gender_service = GenderService(db)
    await gender_service.delete(gender_id)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_gender_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
#     """ api to delete gender data by id. """
#     gender_service = GenderService(db)
#     await gender_service.delete(user_id)
