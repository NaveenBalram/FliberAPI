import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_pan_exempt_category import (
    OutBsePanExemptCategorySchema,
    InBsePanExemptCategorySchema,
    BsePanExemptCategorySchema,
)
from app.service.bse_pan_exempt_category import BsePanExemptCategoryService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_bse_pan_exempt_category(
    payload: InBsePanExemptCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse pan exempt data. """
    bse_pan_exempt_category_service = BsePanExemptCategoryService(db)
    bse_pan_exempt_category = await bse_pan_exempt_category_service.create(payload)
    return bse_pan_exempt_category


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_pan_exempt_category(
    payload: BsePanExemptCategorySchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse pan exempt data. """
    bse_pan_exempt_category_service = BsePanExemptCategoryService(db)
    await bse_pan_exempt_category_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutBsePanExemptCategorySchema,
)
async def get_bse_pan_exempt_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutBsePanExemptCategorySchema:
    """ api to fetch bse pan exempt data by id. """
    bse_pan_exempt_category_service = BsePanExemptCategoryService(db)
    bse_pan_exempt_category = await bse_pan_exempt_category_service.get_by_id(uuid)
    return bse_pan_exempt_category


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_pan_exempt_category(db: AsyncSession = Depends(get_db)):
    """ api to fetch bse pan exempt data. """
    bse_pan_exempt_category_service = BsePanExemptCategoryService(db)
    bse_pan_exempt_category = await bse_pan_exempt_category_service.get_all()
    return bse_pan_exempt_category


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_pan_exempt_category(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete bse pan exempt data by id. """
    bse_pan_exempt_category_service = BsePanExemptCategoryService(db)
    return await bse_pan_exempt_category_service.delete(uuid)

