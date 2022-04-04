import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.advisor import OutAdvisorSchema, InAdvisorSchema
from app.service.advisor import AdvisorService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_advisor(payload: InAdvisorSchema, db: AsyncSession = Depends(get_db)):
    """api to save advisor data."""
    try:
        advisor_service = AdvisorService(db)
        advisor = await advisor_service.create(payload)
        return advisor
    except Exception as e:
        return {"error": str(e)}


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_advisor(payload: OutAdvisorSchema, db: AsyncSession = Depends(get_db)):
    """api to update advisor data."""
    try:
        advisor_service = AdvisorService(db)
        await advisor_service.update(payload)
    except Exception as e:
        return {"error": str(e)}


@router.get(
    "/{advisor_id}",
    status_code=status.HTTP_200_OK,
)
async def get_advisor(advisor_id: UUID, db: AsyncSession = Depends(get_db)):
    """api to fetch advisor data using advisor id."""
    try:
        advisor_service = AdvisorService(db)
        advisor = await advisor_service.get_by_id(advisor_id)
        return advisor
    except Exception as e:
        return {"error": str(e)}


@router.get("/", status_code=status.HTTP_200_OK)
async def get_advisor(db: AsyncSession = Depends(get_db)):
    """api to fetch all advisor data."""
    try:
        advisor_service = AdvisorService(db)
        advisor = await advisor_service.get_all()
        return advisor
    except Exception as e:
        return {"error": str(e)}


@router.delete("/{advisor_id}", status_code=status.HTTP_200_OK)
async def delete_advisor(advisor_id: UUID, db: AsyncSession = Depends(get_db)):
    """api to delete all advisor data using advisor id."""
    try:
        advisor_service = AdvisorService(db)
        return await advisor_service.delete(advisor_id)
    except Exception as e:
        return {"error": str(e)}
