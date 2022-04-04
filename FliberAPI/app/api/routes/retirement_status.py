import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.retirement_status import (
    OutRetirementStatusSchema,
    InRetirementStatusSchema,
    RetirementStatusSchema,
)
from app.service.retirement_status import RetirementStatusService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=OutRetirementStatusSchema
)
async def create_retirement_status(
    payload: InRetirementStatusSchema, db: AsyncSession = Depends(get_db)
) -> OutRetirementStatusSchema:
    """ api to save retirement status data. """
    retirement_status_service = RetirementStatusService(db)
    retirement_status = await retirement_status_service.create(payload)
    return retirement_status


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_retirement_status(
    payload: RetirementStatusSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update retirement status data. """
    retirement_status_service = RetirementStatusService(db)
    await retirement_status_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutRetirementStatusSchema
)
async def get_retirement_status(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutRetirementStatusSchema:
    """ api to get retirement status data by id. """
    retirement_status_service = RetirementStatusService(db)
    retirement_status = await retirement_status_service.get_by_id(uuid)
    return retirement_status


@router.get("/", status_code=status.HTTP_200_OK)
async def get_retirement_status(db: AsyncSession = Depends(get_db)):
    """ api to get retirement status data. """
    retirement_status_service = RetirementStatusService(db)
    retirement_status = await retirement_status_service.get_all()
    return retirement_status


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_retirement_status(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete retirement status data by id. """
    retirement_status_service = RetirementStatusService(db)
    await retirement_status_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_retirement_status_by_user_id(
    user_id: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete retirement status data bu user id. """
    retirement_status_service = RetirementStatusService(db)
    await retirement_status_service.delete(user_id)
