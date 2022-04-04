import datetime
import uuid
from typing import Type
from uuid import UUID

from sqlalchemy.sql.expression import select, update, insert

from app.db.repositories.base import BaseRepository
from app.db.tables.user import User
from app.models.schema.user import (
    InUserSchema,
    UserSchema,
    BseRelatedData,
    LogoutStatus,
    UserRegisterSchema,
    UserStatusSchema,
)


class UserRepository(BaseRepository[InUserSchema, UserSchema, User]):
    @property
    def _in_schema(self) -> Type[InUserSchema]:
        return InUserSchema

    @property
    def _schema(self) -> Type[UserSchema]:
        return UserSchema

    @property
    def _table(self) -> Type[User]:
        return User

    async def register_user(self, payload: UserRegisterSchema):
        user_id = uuid.uuid4()
        stmt = insert(self._table).values(
            Id=user_id,
            FirstName=payload.FirstName,
            LastName=payload.LastName,
            DateOfBirth=payload.DateOfBirth,
            Phone=payload.Phone,
            Email=payload.Email,
            ResidentStatus=payload.ResidentStatus,
            IsActive=True,
            StartDate=datetime.datetime.now(),
            IsMobileNumberValidated=True,
            IsEmailValidated=True,
            CreatedOn=datetime.datetime.now(),
            UpdatedOn=datetime.datetime.now(),
        )

        await self._db_session.execute(stmt)

        result = await self._db_session.execute(
            select(self._table).where(self._table.Id == user_id)
        )
        for item in result.fetchall():
            return item
        return {}

    async def update_user_status(self, payload: UserStatusSchema):
        stmt = (
            update(self._table)
            .values(
                GenderId=payload.GenderId,
                RetirementStatusId=payload.RetirementStatusId,
                MaritalStatusId=payload.MaritalStatusId,
            )
            .where(self._table.Id == payload.UserId)
        )

        return await self._db_session.execute(stmt)

    async def get_by_phone(self, number, email_id):
        query = None
        if number:
            query = self._table.Phone == str(number)
        elif email_id:
            query = self._table.Email == email_id

        result = await self._db_session.execute(
            select(
                self._table.Id,
                self._table.FirstName,
                self._table.LastName,
                self._table.DateOfBirth,
                self._table.ModuleType,
                self._table.Status,
                self._table.LastLogin,
                self._table.StartDate,
                self._table.LifeExpectancy,
                self._table.RetirementAge,
                self._table.ResidentStatus,
                self._table.IsActive,
                self._table.IsEmailValidated,
                self._table.Email,
                self._table.Phone,
                self._table.IMEINumber,
                self._table.GenderId,
                self._table.MaritalStatusId,
                self._table.RetirementStatusId,
                self._table.IsInitialPaymentIsDone,
                self._table.IsPanVerified,
            ).where(query)
        )

        for item in result.fetchall():
            return item
        return {}

    async def find_by_email(self, email):

        result = await self._db_session.execute(
            select(
                self._table.Id,
                self._table.FirstName,
                self._table.LastName,
                self._table.DateOfBirth,
                self._table.ModuleType,
                self._table.Status,
                self._table.LastLogin,
                self._table.StartDate,
                self._table.LifeExpectancy,
                self._table.RetirementAge,
                self._table.ResidentStatus,
                self._table.IsActive,
                self._table.IsEmailValidated,
                self._table.IsEmailValidated,
                self._table.Email,
                self._table.Phone,
                self._table.IMEINumber,
                self._table.GenderId,
                self._table.MaritalStatusId,
                self._table.RetirementStatusId,
                self._table.IsInitialPaymentIsDone,
                self._table.IsPanVerified,
            ).where(self._table.Email == email)
        )

        for item in result.fetchall():
            return item
        return {}

    async def get_dob(self, user_id: UUID):
        result = await self._db_session.execute(
            select(self._table.DateOfBirth).where(self._table.Id == user_id)
        )
        return_items = []
        for item in result.fetchall():
            return_items.append(item[0])

        return return_items

    async def update_bse_data(self, payload: BseRelatedData):
        stmt = (
            update(self._table)
            .values(
                FatherName=payload.FatherName,
                MotherName=payload.MotherName,
                SpouseName=payload.SpouseName,
                SpouseDOB=payload.SpouseDOB,
                SpousePan=payload.SpousePan,
                BornCityId=payload.BornCityId,
                BornStateId=payload.BornStateId,
                Nationality=payload.Nationality,
                SourceOfWealth=payload.SourceOfWealth,
                OccupationTypes=payload.OccupationTypes,
                ResidentStatus=payload.ResidentStatus,
                IncomeSlab=payload.IncomeSlab,
                AddressType=payload.AddressType,
                AddressLine1=payload.AddressLine1,
                AddressLine2=payload.AddressLine2,
                CityId=payload.CityId,
                StateId=payload.StateId,
            )
            .where(self._table.Id == payload.UserId)
        )

        result = await self._db_session.execute(stmt)
        return result

    async def get_bse_data(self, user_id: UUID):

        stmt = select(
            self._table.FatherName,
            self._table.MotherName,
            self._table.SpouseName,
            self._table.SpouseDOB,
            self._table.SpousePan,
            self._table.BornCityId,
            self._table.BornStateId,
            self._table.Nationality,
            self._table.SourceOfWealth,
            self._table.OccupationTypes,
            self._table.ResidentStatus,
            self._table.IncomeSlab,
            self._table.AddressType,
            self._table.AddressLine1,
            self._table.AddressLine2,
            self._table.CityId,
            self._table.StateId,
        ).where(self._table.Id == user_id)

        result = await self._db_session.execute(stmt)
        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        return return_items

    async def get_singzy_data(self, user_id: UUID):

        stmt = select(
            self._table.FirstName,
            self._table.Email,
            self._table.Phone,
            self._table.DateOfBirth,
        ).where(self._table.Id == user_id)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        return return_items

    async def update_logout_status(self, payload: LogoutStatus):
        stmt = (
            update(self._table)
            .values(
                ModuleType=payload.ModuleType,
                Status=payload.Status,
                LastQuestion=payload.LastQuestion,
                LastLogin=datetime.datetime.now(),
            )
            .where(self._table.Id == payload.UserId)
        )

        await self._db_session.execute(stmt)

    async def get_related_age(self, user_id: UUID):
        stmt = select(self._table.RetirementAge, self._table.LifeExpectancy).where(
            self._table.Id == user_id
        )

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        return return_items

    async def get_all_ids(self):
        stmt = select(self._table.Id)

        result = await self._db_session.execute(stmt)

        return_items = []
        for item in result.fetchall():
            return_items.append(item)

        return return_items

    async def get_personal_information(self, user_id):

        stmt = select(
            self._table.Id,
            self._table.SpouseName,
            self._table.MotherName,
            self._table.FatherName,
            self._table.MaritalStatusId,
        ).where(self._table.Id == user_id)

        result = await self._db_session.execute(stmt)

        for item in result.fetchall():
            return item

    async def get_user_address(self, user_id: UUID):

        stmt = select(
            self._table.Id,
            self._table.CityId,
            self._table.BornCityId,
            self._table.AddressType,
            self._table.AddressLine1,
            self._table.AddressLine2,
            self._table.PinCode,
        ).where(self._table.Id == user_id)

        result = await self._db_session.execute(stmt)

        for item in result.fetchall():
            return item

    async def get_user_occupation(self, user_id):

        stmt = select(
            self._table.Id,
            self._table.OccupationTypes,
            self._table.IncomeSlab,
            self._table.SourceOfWealth,
        ).where(self._table.Id == user_id)

        result = await self._db_session.execute(stmt)

        for item in result.fetchall():
            return item
