import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_client_tax_status import (
    OutBseClientTaxStatusSchema,
    InBseClientTaxStatusSchema,
    BseClientTaxStatusSchema,
)
from app.service.bse_client_tax_status import BseClientTaxStatusService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_bse_client_tax_status(
    payload: InBseClientTaxStatusSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client tax status data. """
    bse_client_tax_status_service = BseClientTaxStatusService(db)
    bse_client_tax_status = await bse_client_tax_status_service.create(payload)
    return bse_client_tax_status


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_client_tax_status(
    payload: BseClientTaxStatusSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse client tax status data. """
    bse_client_tax_status_service = BseClientTaxStatusService(db)
    await bse_client_tax_status_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK
)
async def get_bse_client_tax_status(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse client tax status data by id. """
    bse_client_tax_status_service = BseClientTaxStatusService(db)
    bse_client_tax_status = await bse_client_tax_status_service.get_by_id(uuid)
    return bse_client_tax_status


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_client_tax_status(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse client tax status data. """
    bse_client_tax_status_service = BseClientTaxStatusService(db)
    bse_client_tax_status = await bse_client_tax_status_service.get_all()
    return bse_client_tax_status


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_client_tax_status(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse client tax status data by id. """
    bse_client_tax_status_service = BseClientTaxStatusService(db)
    return await bse_client_tax_status_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_bse_client_tax_status_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to delete bse client tax status data. """
#     bse_client_tax_status_service = BseClientTaxStatusService(db)
#     return await bse_client_tax_status_service.delete(user_id)
