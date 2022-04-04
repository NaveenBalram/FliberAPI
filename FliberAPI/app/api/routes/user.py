import logging
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from app.api.dependencies.db import get_db
from app.models.schema.user import (
    InUserSchema,
    UserSchema,
    BseRelatedData,
    LogoutStatus,
    UserRegisterSchema,
    UserStatusSchema,
    UserPhoneSchema,
)
from app.service.user import UserService

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(payload: InUserSchema, db: AsyncSession = Depends(get_db)):
    """ api to save user data. """
    user_service = UserService(db)
    print(payload)
    user = await user_service.create(payload)
    return user


@router.patch("/", status_code=status.HTTP_200_OK)
async def update_user(payload: UserSchema, db: AsyncSession = Depends(get_db)):
    """ api to update user data. """
    user_service = UserService(db)
    return await user_service.update(payload)


@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
async def get_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get user data by user id. """
    user_service = UserService(db)
    user = await user_service.get_by_id(user_id)
    return user


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(db: AsyncSession = Depends(get_db)):
    """ api to get user data. """
    user_service = UserService(db)
    user = await user_service.get_all()
    return user


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user data by user id. """
    user_service = UserService(db)
    await user_service.delete(user_id)


@router.post("/by/", status_code=status.HTTP_200_OK)
async def get_by_phone_number(
    payload: UserPhoneSchema, db: AsyncSession = Depends(get_db)
):
    """ api to save user data. """
    user_service = UserService(db)
    return await user_service.get_by_phone_number(payload.PhoneNumber, payload.EmailId)


@router.patch("/add/bse/data", status_code=status.HTTP_200_OK)
async def update_bse_information(
    payload: BseRelatedData, db: AsyncSession = Depends(get_db)
):
    """ api to update bse user data. """
    user_service = UserService(db)
    return await user_service.update_bse_user(payload)


@router.get("/get/bse/data", status_code=status.HTTP_200_OK)
async def get_bse_information(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get bse user data by user_id. """
    user_service = UserService(db)
    return await user_service.get_bse_user(user_id)


@router.post("/logout/status", status_code=status.HTTP_200_OK)
async def update_logout_status(
    payload: LogoutStatus, db: AsyncSession = Depends(get_db)
):
    """ api to logout user. """
    user_service = UserService(db)
    return await user_service.update_logout_status(payload)


@router.post("/register", status_code=status.HTTP_200_OK)
async def registration(
    payload: UserRegisterSchema, db: AsyncSession = Depends(get_db)
):
    """ api to register user. """
    user_service = UserService(db)
    return await user_service.register_user(payload)


@router.post("/update/satus", status_code=status.HTTP_200_OK)
async def update_status(
    payload: UserStatusSchema, db: AsyncSession = Depends(get_db)
):
    """ api to update user status. """
    user_service = UserService(db)
    return await user_service.update_user_status(payload)


@router.get("/personal/information", status_code=status.HTTP_200_OK)
async def get_personal_information(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get user data by user_id. """
    user_service = UserService(db)
    return await user_service.get_user_personal_information(user_id)


@router.get("/address/", status_code=status.HTTP_200_OK)
async def get_user_address(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get user data by user_id. """
    user_service = UserService(db)
    return await user_service.get_user_address(user_id)


@router.get("/occupation/", status_code=status.HTTP_200_OK)
async def get_occupation_data(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to get bse user occupation data by user id. """
    user_service = UserService(db)
    return await user_service.get_user_occupation(user_id)


@router.delete("/by/user/id/", status_code=status.HTTP_200_OK)
async def delete_user_by_user_id(user_id: UUID, db: AsyncSession = Depends(get_db)):
    """ api to delete user data by user id. """
    user_service = UserService(db)
    await user_service.delete(user_id)
