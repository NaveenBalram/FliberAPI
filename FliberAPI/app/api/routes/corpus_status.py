import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.corpus_status import (
    OutCorpusStatusSchema,
    InCorpusStatusSchema,
    CorpusStatusSchema,
)
from app.service.corpus_status import CorpusStatusService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_corpus_status(
    payload: InCorpusStatusSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save corpus status data."""
    corpus_status_service = CorpusStatusService(db)
    corpus_status = await corpus_status_service.create(payload)
    return corpus_status


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_corpus_status(
    payload: CorpusStatusSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update corpus status data."""
    corpus_status_service = CorpusStatusService(db)
    await corpus_status_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK
)
async def get_corpus_status(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch corpus status data by id."""
    corpus_status_service = CorpusStatusService(db)
    corpus_status = await corpus_status_service.get_by_id(uuid)
    return corpus_status


@router.get("/", status_code=status.HTTP_200_OK)
async def get_corpus_status(db: AsyncSession = Depends(get_db)):
    """ api to fetch all corpus status data."""
    corpus_status_service = CorpusStatusService(db)
    corpus_status = await corpus_status_service.get_all()
    return corpus_status


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_corpus_status(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete corpus status data by id."""
    corpus_status_service = CorpusStatusService(db)
    return await corpus_status_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_corpus_status_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to delete corpus status data by user id."""
#     corpus_status_service = CorpusStatusService(db)
#     return await corpus_status_service.delete(user_id)
