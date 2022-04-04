import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.bse_client_nominee import (
    OutBseClientNomineeSchema,
    InBseClientNomineeSchema,
    BseClientNomineeSchema,
)
from app.service.bse_client_nominee import BseClientNomineeService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/", status_code=status.HTTP_201_CREATED
)
async def create_bse_client_nominee(
        payload: InBseClientNomineeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client nominee data. """
    bse_client_nominee_service = BseClientNomineeService(db)
    bse_client_nominee = await bse_client_nominee_service.create(payload)
    return bse_client_nominee


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_bse_client_nominee(
        payload: BseClientNomineeSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save bse client nominee data. """
    bse_client_nominee_service = BseClientNomineeService(db)
    await bse_client_nominee_service.update(payload)


@router.get(
    "/{uuid}", status_code=status.HTTP_200_OK,
)
async def get_bse_client_nominee(
        uuid: UUID, db: AsyncSession = Depends(get_db)
):
    """ api to fetch bse client nominee data id """
    bse_client_nominee_service = BseClientNomineeService(db)
    bse_client_nominee = await bse_client_nominee_service.get_by_id(uuid)
    return bse_client_nominee


@router.get("/", status_code=status.HTTP_200_OK)
async def get_bse_client_nominee(db: AsyncSession = Depends(get_db)):
    """ api to fetch bse client nominee data. """
    bse_client_nominee_service = BseClientNomineeService(db)
    bse_client_nominee = await bse_client_nominee_service.get_all()
    return bse_client_nominee


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_bse_client_nominee(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delet bse client nominee data by id. """
    bse_client_nominee_service = BseClientNomineeService(db)
    await bse_client_nominee_service.delete(uuid)


@router.delete("/by/{user_id}", status_code=status.HTTP_200_OK)
async def delete_bse_client_nominee(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to save bse client nominee data by user id. """
    bse_client_nominee_service = BseClientNomineeService(db)
    return await bse_client_nominee_service.delete_by_user_id(user_id)




