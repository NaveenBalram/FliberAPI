import logging
from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from app.core.utility import encrypt_data
from app.db.repositories.user import UserRepository
from app.db.repositories.user_info import UserInfoRepository
from app.models.schema.user import (
    OutUserSchema,
    InUserSchema,
    UserSchema,
    BseRelatedData,
    LogoutStatus,
    UserRegisterSchema,
    UserStatusSchema,
)
from app.models.schema.user_info import InUserInfoSchema

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._user_repository = UserRepository(self._db_session)

    async def create(self, payload: InUserSchema):
        user_info = UserInfoRepository(self._db_session)

        # verify email exists.
        if await self._user_repository.find_by_email(payload.Email):
            raise ValueError("Email already registered")

        # verify 10-digit phone number is passed.
        if len(payload.Phone) != 10:
            raise ValueError("Enter 10 digit phone number")

        if not payload.Phone.isdigit():
            raise ValueError("Enter 10 digit phone number")

        if payload.ResidentStatus.lower() != "indian":
            raise ValueError("Only available for Indian users.")

        # verify mobile number already exist
        if await self._user_repository.get_by_phone(payload.Phone, payload.Email):
            raise ValueError("Mobile number already registered")

        # encrypt the password
        key, password = encrypt_data(payload.Password)
        payload.Password = password.decode()

        # save the user data
        user = await self._user_repository.create(payload)

        # save the key generated to encrypt and decrypt the password
        await user_info.create(InUserInfoSchema(UserId=user.Id, Text=key))

        return user

    async def get_by_id(self, user_id: UUID) -> OutUserSchema:
        user = await self._user_repository.get_by_id(user_id)
        return user

    async def get_all(self):
        users = await self._user_repository.get_all()
        return users

    async def delete(self, user_id: UUID):
        await self._user_repository.delete(user_id)

    async def update(self, payload: UserSchema):
        await self._user_repository.update(payload)

    async def get_by_phone_number(self, number, email_id):
        if not number and not email_id:
            return "Phone number or email id is must."
        user = await self._user_repository.get_by_phone(number, email_id)
        return user

    async def update_bse_user(self, user_data: BseRelatedData):
        user = await self._user_repository.update_bse_data(user_data)
        return user

    async def get_bse_user(self, user_id: UUID):
        user = await self._user_repository.get_bse_data(user_id)
        return user

    async def update_logout_status(self, payload: LogoutStatus):
        return await self._user_repository.update_logout_status(payload)

    async def get_user_personal_information(self, user_id: UUID):
        return await self._user_repository.get_personal_information(user_id)

    async def register_user(self, payload: UserRegisterSchema):

        # verify email exists.
        if await self._user_repository.find_by_email(payload.Email):
            raise ValueError("Email already registered")

        # verify 10-digit phone number is passed.
        if len(payload.Phone) != 10:
            raise ValueError("Enter 10 digit phone number")

        if not payload.Phone.isdigit():
            raise ValueError("Enter 10 digit phone number")

        if payload.ResidentStatus.lower() != "indian":
            raise ValueError("Only available for Indian users.")

        # verify mobile number already exist
        if await self._user_repository.get_by_phone(payload.Phone, payload.Email):
            raise ValueError("Mobile number already registered")

        # save the user data
        return await self._user_repository.register_user(payload)

    async def update_user_status(self, payload: UserStatusSchema):
        await self._user_repository.update_user_status(payload)

    async def get_user_occupation(self, user_id: UUID):
        return await self._user_repository.get_user_occupation(user_id)

    async def get_user_address(self, user_id: UUID):
        return await self._user_repository.get_user_address(user_id)

    async def delete_user_by_user_id(self, user_id: UUID):
        await self._user_repository.delete_by_user_id(user_id)
