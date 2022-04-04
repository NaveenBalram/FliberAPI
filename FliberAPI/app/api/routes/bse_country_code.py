import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_country_code import (
    OutBseCountryCodeSchema,
    InBseCountryCodeSchema,
    BseCountryCodeSchema,
)
from app.service.bse_country_code import BseCountryCodeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED,
)
async def create_bse_country_code(
    payload: InBseCountryCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse country data. """
    bse_country_code_service = BseCountryCodeService(db)
    bse_country_code = await bse_country_code_service.create(payload)
    return bse_country_code


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_country_code(
    payload: BseCountryCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse country data. """
    bse_country_code_service = BseCountryCodeService(db)
    await bse_country_code_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK, response_model=OutBseCountryCodeSchema
)
async def get_bse_country_code(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get bse country data by id. """
    bse_country_code_service = BseCountryCodeService(db)
    bse_country_code = await bse_country_code_service.get_by_id(uuid)
    return bse_country_code


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_country_code(db: AsyncSession = Depends(get_db)):
    """ api to fetch all bse country data. """
    bse_country_code_service = BseCountryCodeService(db)
    bse_country_code = await bse_country_code_service.get_all()
    return bse_country_code


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_country_code(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete bse country data by id. """
    bse_country_code_service = BseCountryCodeService(db)
    return await bse_country_code_service.delete(uuid)

