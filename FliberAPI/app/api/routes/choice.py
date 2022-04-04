import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.choice import OutChoiceSchema, InChoiceSchema, ChoiceSchema
from app.service.choice import ChoiceService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_choice(
    payload: InChoiceSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save choice data for questions. """
    choice_service = ChoiceService(db)
    choice = await choice_service.create(payload)
    return choice


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_choice(payload: ChoiceSchema, db: AsyncSession = Depends(get_db)):
    """ api to save choice data for questions. """
    choice_service = ChoiceService(db)
    await choice_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutChoiceSchema)
async def get_choice(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutChoiceSchema:
    """ api to update choice data for questions. """
    choice_service = ChoiceService(db)
    choice = await choice_service.get_by_id(uuid)
    return choice


@router.get("/", status_code=status.HTTP_200_OK)
async def get_choice(db: AsyncSession = Depends(get_db)):
    """ api to save choice data for questions. """
    choice_service = ChoiceService(db)
    choice = await choice_service.get_all()
    return choice


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_choice(uuid: UUID, db: AsyncSession = Depends(get_db)):
    choice_service = ChoiceService(db)
    return await choice_service.delete(uuid)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_choice_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    choice_service = ChoiceService(db)
    return await choice_service.delete(user_id)
