import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_client_occupation_code import (
    OutBseClientOccupationCodeSchema,
    InBseClientOccupationCodeSchema,
    BseClientOccupationCodeSchema,
)
from app.service.bse_client_occupation_code import BseClientOccupationCodeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_bse_client_occupation_code(
    payload: InBseClientOccupationCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client occupation code data. """
    bse_client_occupation_code_service = BseClientOccupationCodeService(db)
    bse_client_occupation_code = await bse_client_occupation_code_service.create(
        payload
    )
    return bse_client_occupation_code


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_client_occupation_code(
    payload: BseClientOccupationCodeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update bse client occupation code data. """
    bse_client_occupation_code_service = BseClientOccupationCodeService(db)
    await bse_client_occupation_code_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK
)
async def get_bse_client_occupation_code(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to get bse client occupation code data by id. """
    bse_client_occupation_code_service = BseClientOccupationCodeService(db)
    bse_client_occupation_code = await bse_client_occupation_code_service.get_by_id(
        uuid
    )
    return bse_client_occupation_code


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_client_occupation_code(db: AsyncSession = Depends(get_db)):
    """ api to get all bse client occupation code data. """
    bse_client_occupation_code_service = BseClientOccupationCodeService(db)
    bse_client_occupation_code = await bse_client_occupation_code_service.get_all()
    return bse_client_occupation_code


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_client_occupation_code(
    uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to delete bse client occupation code data by id. """
    bse_client_occupation_code_service = BseClientOccupationCodeService(db)
    return await bse_client_occupation_code_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_bse_client_occupation_code_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to delete bse client occupation code data by user id. """
#     bse_client_occupation_code_service = BseClientOccupationCodeService(db)
#     return await bse_client_occupation_code_service.delete(user_id)
