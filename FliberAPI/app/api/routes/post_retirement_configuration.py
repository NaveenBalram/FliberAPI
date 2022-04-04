import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.post_retirement_configuration import (
    OutPostRetirementConfigurationSchema,
    InPostRetirementConfigurationSchema,
    PostRetirementConfigurationSchemaBase,
    PostRetirementConfigurationSchema,
)
from app.service.post_retirement_configuration import PostRetirementConfigurationService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutPostRetirementConfigurationSchema,
)
async def create_post_retirement_configuration(
    payload: InPostRetirementConfigurationSchema, db: AsyncSession = Depends(get_db)
) -> OutPostRetirementConfigurationSchema:
    """ api to save post retirement configuration data. """
    post_retirement_configuration_service = PostRetirementConfigurationService(db)
    post_retirement_configuration = await post_retirement_configuration_service.create(
        payload
    )
    return post_retirement_configuration


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_post_retirement_configuration(
    payload: PostRetirementConfigurationSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update post retirement configuration data. """
    post_retirement_configuration_service = PostRetirementConfigurationService(db)
    await post_retirement_configuration_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutPostRetirementConfigurationSchema,
)
async def get_post_retirement_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get post retirement configuration data by id. """
    post_retirement_configuration_service = PostRetirementConfigurationService(db)
    post_retirement_configuration = (
        await post_retirement_configuration_service.get_by_id(uuid)
    )
    return post_retirement_configuration


@router.get("/", status_code=status.HTTP_200_OK)
async def get_post_retirement_configuration(db: AsyncSession = Depends(get_db)):
    """ api to get post retirement configuration data. """
    post_retirement_configuration_service = PostRetirementConfigurationService(db)
    post_retirement_configuration = (
        await post_retirement_configuration_service.get_all()
    )
    return post_retirement_configuration


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_post_retirement_configuration(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to  post retirement configuration data. """
    post_retirement_configuration_service = PostRetirementConfigurationService(db)
    await post_retirement_configuration_service.delete(uuid)

