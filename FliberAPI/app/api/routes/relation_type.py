import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.relation_type import (
    OutRelationTypeSchema,
    InRelationTypeSchema,
    RelationTypeSchema,
)
from app.service.relation_type import RelationTypeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutRelationTypeSchema
)
async def create_relation_type(
    payload: InRelationTypeSchema, db: AsyncSession = Depends(get_db)
) -> OutRelationTypeSchema:
    """ api to save relation type data. """
    relation_type_service = RelationTypeService(db)
    relation_type = await relation_type_service.create(payload)
    return relation_type


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_relation_type(
    payload: RelationTypeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update relation type data. """
    relation_type_service = RelationTypeService(db)
    await relation_type_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutRelationTypeSchema
)
async def get_relation_type(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutRelationTypeSchema:
    """ api to get relation type data by id. """
    relation_type_service = RelationTypeService(db)
    relation_type = await relation_type_service.get_by_id(uuid)
    return relation_type


@router.get("/", status_code=status.HTTP_200_OK)
async def get_relation_type(db: AsyncSession = Depends(get_db)):
    """ api to get relation type data. """
    relation_type_service = RelationTypeService(db)
    relation_type = await relation_type_service.get_all()
    return relation_type


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_relation_type(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete relation type data by id. """
    relation_type_service = RelationTypeService(db)
    await relation_type_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_relation_type_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to delete relation type data by id. """
#     relation_type_service = RelationTypeService(db)
#     await relation_type_service.delete(user_id)
