import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.occupation_types import (
    OutOccupationTypesSchema,
    InOccupationTypesSchema,
    OccupationTypesSchema,
)
from app.service.occupation_types import OccupationTypesService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutOccupationTypesSchema
)
async def create_occupation_types(
    payload: InOccupationTypesSchema, db: AsyncSession = Depends(get_db)
) -> OutOccupationTypesSchema:
    """ api to save occupation types data. """
    occupation_types_service = OccupationTypesService(db)
    occupation_types = await occupation_types_service.create(payload)
    return occupation_types


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_occupation_types(
    payload: OccupationTypesSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update occupation types data. """
    occupation_types_service = OccupationTypesService(db)
    await occupation_types_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutOccupationTypesSchema
)
async def get_occupation_types(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutOccupationTypesSchema:
    """ api to get occupation types data. """
    occupation_types_service = OccupationTypesService(db)
    occupation_types = await occupation_types_service.get_by_id(uuid)
    return occupation_types


@router.get("/", status_code=status.HTTP_200_OK)
async def get_occupation_types(db: AsyncSession = Depends(get_db)):
    """ api to get occupation types data. """
    occupation_types_service = OccupationTypesService(db)
    occupation_types = await occupation_types_service.get_all()
    return occupation_types


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_occupation_types(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete occupation types data by id. """
    occupation_types_service = OccupationTypesService(db)
    await occupation_types_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_occupation_types_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to  occupation types data. """
#     occupation_types_service = OccupationTypesService(db)
#     await occupation_types_service.delete(user_id)
