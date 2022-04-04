import logging
from datetime import datetime
from uuid import UUID

import requests
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.sign_zy import SignZyRepository
from app.db.repositories.signzy_account import SignzyAccountRepository
from app.db.repositories.signzy_users import SignzyUsersRepository
from app.db.repositories.user import UserRepository
from app.models.schema.sign_zy import InSignZySchema, SignZySchema
from app.models.schema.signzy_users import InSignzyUsersSchema

logger = logging.getLogger(__name__)


class SignZyService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._sign_zy_repository = SignZyRepository(self._db_session)

    async def create(self, payload: InSignZySchema):
        sign_zy = await self._sign_zy_repository.create(payload)

        return sign_zy

    async def get_by_id(self, uuid: UUID):
        sign_zy = await self._sign_zy_repository.get_by_id(uuid)
        return sign_zy

    async def get_all(self):
        sign_zy = await self._sign_zy_repository.get_all()
        return sign_zy

    async def delete(self, uuid: UUID):
        await self._sign_zy_repository.delete(uuid)

    async def update(self, payload: SignZySchema):
        await self._sign_zy_repository.update(payload)

    async def signzy_response(self, user_id: UUID):

        signzy_user_repository = SignzyUsersRepository(self._db_session)

        result = await signzy_user_repository.get_by_user_id(user_id)

        if result:
            return result

        signzy_account_repository = SignzyAccountRepository(self._db_session)

        sign_credentials = await signzy_account_repository.get_all()
        sign_credentials = sign_credentials[0]

        if sign_credentials is None:
            return "Signzy account details not found."

        payload = {
            "username": sign_credentials["UserName"],
            "password": sign_credentials["Password"],
        }

        headers = {"Content-Type": "application/json"}

        url = "https://multi-channel-preproduction.signzy.tech/api/channels/login"

        response = requests.request("POST", url, json=payload, headers=headers).json()

        data = InSignZySchema(
            UserId=user_id,
            SignZyId=response["userId"],
            Token=response["id"],
            TTL=response["ttl"],
            CreatedOn=datetime.now(),
            UpdatedOn=datetime.now(),
        )
        await self._sign_zy_repository.create(data)

        headers = {"Content-Type": "application/json", "Authorization": response["id"]}

        user_repository = UserRepository(self._db_session)
        user_data = await user_repository.get_singzy_data(user_id)
        user_data = user_data[0]

        payload = {
            "username": str(user_data.FirstName).lower()
                        + str(user_data.DateOfBirth).replace("-", "").split(" ", maxsplit=1)[0]
                        + str(datetime.now())
                            .replace("-", "")
                            .replace(":", "")
                            .replace(" ", "")
                            .split(".", maxsplit=1)[0],
            "name": user_data.FirstName,
            "phone": user_data.Phone,
            "email": user_data.Email,
        }

        url = f"https://multi-channel-preproduction.signzy.tech/api/channels/{response['userId']}/onboardings"
        response = requests.request("POST", url, json=payload, headers=headers).json()

        if response.get("error", False):
            return response["error"]

        response = response["createdObj"]

        data = InSignzyUsersSchema(
            UserId=user_id,
            Email=response["email"],
            Phone=response["phone"],
            Name=response["name"],
            UserName=response["username"],
            ResponseId=response["id"],
            CustomerId=response["customerId"],
            ChannelId=response["channelInfo"]["id"],
            ChannelUserName=response["channelInfo"]["username"],
            ChannelName=response["channelInfo"]["name"],
            ApplicationUrl=response["applicationUrl"],
            MobileLoginUrl=response["mobileLoginUrl"],
            AutoLoginUrl=response["autoLoginUrL"],
            MobileAutoLoginUrl=response["mobileAutoLoginUrl"],
        )

        await signzy_user_repository.create(data)

        return {
            "ApplicationUrl": response["applicationUrl"],
            "MobileLoginUrl": response["mobileLoginUrl"],
            "AutoLoginUrl": response["autoLoginUrL"],
            "MobileAutoLoginUrl": response["mobileAutoLoginUrl"],
        }

    async def delete_sign_zy_by_user_id(self, user_id: UUID):
        await self._sign_zy_repository.delete_by_user_id(user_id)
