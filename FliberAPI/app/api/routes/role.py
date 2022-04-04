import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.role import OutRoleSchema, InRoleSchema, RoleSchema
from app.service.role import RoleService

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=OutRoleSchema)
async def create_role(
    payload: InRoleSchema, db: AsyncSession = Depends(get_db)
) -> OutRoleSchema:
    """ api to save role data. """
    role_service = RoleService(db)
    role = await role_service.create(payload)
    return role


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_role(payload: RoleSchema, db: AsyncSession = Depends(get_db)):
    """ api to update role data. """
    role_service = RoleService(db)
    await role_service.update(payload)


@router.get("/{uuid}", status_code=status.HTTP_200_OK, response_model=OutRoleSchema)
async def get_role(uuid: UUID, db: AsyncSession = Depends(get_db)) -> OutRoleSchema:
    """ api to get role data by id. """
    role_service = RoleService(db)
    role = await role_service.get_by_id(uuid)
    return role


@router.get("/", status_code=status.HTTP_200_OK)
async def get_role(db: AsyncSession = Depends(get_db)):
    """ api to get role data. """
    role_service = RoleService(db)
    role = await role_service.get_all()
    return role


@router.delete("/{uuid}", status_code=status.HTTP_200_OK)
async def delete_role(uuid: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete role data by id. """
    role_service = RoleService(db)
    await role_service.delete(uuid)

