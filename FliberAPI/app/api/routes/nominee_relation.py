import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.nominee_relation import (
    OutNomineeRelationSchema,
    InNomineeRelationSchema,
    NomineeRelationSchema,
)
from app.service.nominee_relation import NomineeRelationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutNomineeRelationSchema
)
async def create_nominee_relation(
    payload: InNomineeRelationSchema, db: AsyncSession = Depends(get_db)
) -> OutNomineeRelationSchema:
    """ api to save nominee relation data. """
    nominee_relation_service = NomineeRelationService(db)
    nominee_relation = await nominee_relation_service.create(payload)
    return nominee_relation


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_nominee_relation(
    payload: NomineeRelationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update nominee relation data. """
    nominee_relation_service = NomineeRelationService(db)
    await nominee_relation_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutNomineeRelationSchema
)
async def get_nominee_relation(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutNomineeRelationSchema:
    """ api to get nominee relation data. """
    nominee_relation_service = NomineeRelationService(db)
    nominee_relation = await nominee_relation_service.get_by_id(uuid)
    return nominee_relation


@router.get("/", status_code=status.HTTP_200_OK)
async def get_nominee_relation(db: AsyncSession = Depends(get_db)):
    """ api to get nominee relation data. """
    nominee_relation_service = NomineeRelationService(db)
    nominee_relation = await nominee_relation_service.get_all()
    return nominee_relation


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_nominee_relation(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete nominee relation data by id. """
    nominee_relation_service = NomineeRelationService(db)
    await nominee_relation_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_nominee_relation_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete nominee relation data by user id. """
    nominee_relation_service = NomineeRelationService(db)
    await nominee_relation_service.delete(user_id)
