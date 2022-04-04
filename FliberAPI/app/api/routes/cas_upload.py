import logging
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.cas_upload import InCasUploadSchema, CasUploadSchema
from app.service.cas_upload import CasUploadService
from app.service.cas_upload_logic.cas_upload import scrap_cas

router = APIRouter()
logger = logging.getLogger(__name__)


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_cas_upload(payload: InCasUploadSchema, db: AsyncSession = Depends(get_db)):
#     cas_upload_service = CasUploadService(db)
#     cas_upload = await cas_upload_service.create(payload)
#     return cas_upload
#
#
# @router.patch("/", status_code=status.HTTP_200_OK)
# async def update_cas_upload(payload: CasUploadSchema, db: AsyncSession = Depends(get_db)):
#     cas_upload_service = CasUploadService(db)
#     await cas_upload_service.update(payload)
#
#
# @router.get("/{uuid}", status_code=status.HTTP_200_OK)
# async def get_cas_upload(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     cas_upload_service = CasUploadService(db)
#     cas_upload = await cas_upload_service.get_by_id(uuid)
#     return cas_upload
#
#
# @router.get("/", status_code=status.HTTP_200_OK)
# async def get_cas_upload(db: AsyncSession = Depends(get_db)):
#     cas_upload_service = CasUploadService(db)
#     cas_upload = await cas_upload_service.get_all()
#     return cas_upload
#
#
# @router.delete("/{uuid}", status_code=status.HTTP_200_OK)
# async def delete_cas_upload(uuid: UUID, db: AsyncSession = Depends(get_db)):
#     cas_upload_service = CasUploadService(db)
#     await cas_upload_service.delete(uuid)


@router.get("/upload/cash/", status_code=status.HTTP_200_OK)
def get_cas_upload(email_id: str, password: str, db: AsyncSession = Depends(get_db)):
    return scrap_cas(email_id, password)

