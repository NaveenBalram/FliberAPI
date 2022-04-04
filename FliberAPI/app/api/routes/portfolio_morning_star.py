import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.portfolio_morning_star import (
    OutPortfolioMorningStarSchema,
    InPortfolioMorningStarSchema,
    PortfolioMorningStarSchema,
)
from app.service.portfolio_morning_star import PortfolioMorningStarService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=OutPortfolioMorningStarSchema,
)
async def create_portfolio_morning_star(
    payload: InPortfolioMorningStarSchema, db: AsyncSession = Depends(get_db)
) -> OutPortfolioMorningStarSchema:
    """ api to save portfolio morning star data. """
    portfolio_morning_star_service = PortfolioMorningStarService(db)
    portfolio_morning_star = await portfolio_morning_star_service.create(payload)
    return portfolio_morning_star


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_portfolio_morning_star(
    payload: PortfolioMorningStarSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update portfolio morning star data. """
    portfolio_morning_star_service = PortfolioMorningStarService(db)
    await portfolio_morning_star_service.update(payload)


@router.get(
    "/{uuid}",
    status_code=status.HTTP_200_OK,
    response_model=OutPortfolioMorningStarSchema,
)
async def get_portfolio_morning_star(
    uuid: UUID, db: AsyncSession = Depends(get_db)
) -> OutPortfolioMorningStarSchema:
    """ api to get portfolio morning star data by id. """
    portfolio_morning_star_service = PortfolioMorningStarService(db)
    portfolio_morning_star = await portfolio_morning_star_service.get_by_id(uuid)
    return portfolio_morning_star


@router.get("/", status_code=status.HTTP_200_OK)
async def get_portfolio_morning_star(db: AsyncSession = Depends(get_db)):
    """ api to get portfolio morning star data. """
    portfolio_morning_star_service = PortfolioMorningStarService(db)
    portfolio_morning_star = await portfolio_morning_star_service.get_all()
    return portfolio_morning_star


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_portfolio_morning_star(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete portfolio morning star data by id. """
    portfolio_morning_star_service = PortfolioMorningStarService(db)
    await portfolio_morning_star_service.delete(uuid)


# @router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
# async def delete_portfolio_morning_star_by_user_id(
#     user_id: UUID, db: AsyncSession = Depends(get_db)
# ):
#     """ api to  portfolio morning star data. """
#     portfolio_morning_star_service = PortfolioMorningStarService(db)
#     await portfolio_morning_star_service.delete(user_id)
