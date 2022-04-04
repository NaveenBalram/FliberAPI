import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.sign_zy import OutSignZySchema, InSignZySchema, SignZySchema
from app.service.sign_zy import SignZyService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutSignZySchema)
async def create_sign_zy(
    payload: InSignZySchema, db: AsyncSession = Depends(get_db)
) -> OutSignZySchema:
    """ api to save sign zy data. """
    sign_zy_service = SignZyService(db)
    sign_zy = await sign_zy_service.create(payload)
    return sign_zy


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_sign_zy(payload: SignZySchema, db: AsyncSession = Depends(get_db)):
    """ api to update sign zy data. """
    sign_zy_service = SignZyService(db)
    await sign_zy_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutSignZySchema)
async def get_sign_zy(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutSignZySchema:
    """ api to get sign zy data by id. """
    sign_zy_service = SignZyService(db)
    sign_zy = await sign_zy_service.get_by_id(uuid)
    return sign_zy


@router.get("/", status_code=status.HTTP_200_OK)
async def get_sign_zy(db: AsyncSession = Depends(get_db)):
    """ api to get sign zy data. """
    sign_zy_service = SignZyService(db)
    sign_zy = await sign_zy_service.get_all()
    return sign_zy


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_sign_zy(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete sign zy data by id. """
    sign_zy_service = SignZyService(db)
    await sign_zy_service.delete(uuid)


@router.get("/signzy/response/", status_code=status.HTTP_200_OK)
async def get_signzy_response(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get sign zy data by user_id. """
    sign_zy_service = SignZyService(db)
    return await sign_zy_service.signzy_response(user_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_sign_zy_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete sign zy data by user_id. """
    sign_zy_service = SignZyService(db)
    await sign_zy_service.delete(user_id)
