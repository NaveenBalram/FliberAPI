from datetime import datetime
from uuid import UUID

import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.asset_type import AssetTypeRepository
from app.db.repositories.assets_limit import AssetsLimitRepository
from app.db.repositories.funds_category import FundsCategoryRepository
from app.db.repositories.morning_star_navs import MorningStarNavsRepository
from app.db.repositories.target_assets import TargetAssetsRepository
from app.db.repositories.user import UserRepository
from app.db.repositories.user_assets import UserAssetsRepository
from app.db.repositories.users_re_balance_sheet import UsersReBalanceSheetRepository


class Portfolio:
    def __init__(self, db_session: AsyncSession):
        self._db_session = db_session

    async def get_asset_type(self):
        """Method to get the assets."""

        asset_type = AssetTypeRepository(self._db_session)
        asset_type = await asset_type.get_all()

        return dict((str(x["Id"]), x["Name"]) for x in asset_type)

    async def get_asset_limit(self, asset_type):
        """Method to get the asset limit."""

        asset_limits = AssetsLimitRepository(self._db_session)
        asset_limits = await asset_limits.get_all()
        return dict((asset_type[str(x["AssetTypeId"])], x) for x in asset_limits)

    async def get_navs(self):
        """Method to get ass net asset value."""

        navs_repository = MorningStarNavsRepository(self._db_session)
        navs = await navs_repository.get_all()
        return dict((x["FundName"], x) for x in navs)

    async def get_assets(self, user_id: UUID):
        """Method to get funds allocated to a user."""

        user_assets = UserAssetsRepository(self._db_session)
        return await user_assets.get_by_user_id(user_id)

    async def fund_level_percentage(self, rp_type, amount):
        """Method to fetch the funds target percent.

        return: dict, dictionary containing funds target percent data
        """

        fund_level_percent = FundsCategoryRepository(self._db_session)
        fund_data = await fund_level_percent.get_by_type(rp_type, amount)
        return dict((x["FundName"], x["FundPercent"]) for x in fund_data)

    async def generate_portfolio(self, user_data):
        """Method to generate daily portfolio for a user and check whether rebalance is required."""

        # initialize repositories
        target_asset_repository = TargetAssetsRepository(self._db_session)
        user_balance_repository = UsersReBalanceSheetRepository(self._db_session)
        user_repository = UserRepository(self._db_session)

        # fetch all the asset types
        asset_type = await self.get_asset_type()

        # get all the bound for the asset
        # asset_limits = await self.get_asset_limit(asset_type)

        # get all the update nav for current day
        navs = await self.get_navs()

        # get all user data except whose transaction and rebalance status is 'InProgress'
        user = await user_balance_repository.get_all_by_status(user_data)

        # get the user asset data
        assets = await self.get_assets(user["UserId"])

        # total_amount = 0

        # fetch the date of birth
        dob = await user_repository.get_dob(user["UserId"])
        today = datetime.now().today()

        # find the user age
        userAge = (
            today.year
            - dob[0].year
            - ((today.month, today.day) < (dob[0].month, dob[0].day))
        )

        # fetch the retirement age
        related_age = await user_repository.get_related_age(user["UserId"])
        retirement_age = related_age[0][0]

        # fetch the target asset assigned to user
        target_asset = await target_asset_repository.get_by_id(user["TargetAssetsId"])

        # fetch the age limit by target type
        age_limits = await target_asset_repository.get_limit_by_type(
            target_asset["Type"]
        )
        age_limit = age_limits[0][0]

        # if retirement age - user age  is 1 year closer to age limit.
        if (
            age_limit != 0
            and (retirement_age - userAge) > age_limit
            and (retirement_age - userAge) - age_limit <= 1
        ):
            target_asset_type = target_asset["Type"]
            target_asset = target_asset_type.split("_", maxsplit=1)[0]
            target_asset_type = f"{target_asset}_{age_limit - 5}"

            target_assets = await target_asset_repository.get_by_age_limit(
                age_limit - 1, target_asset_type, user["Amount"]
            )

            await user_balance_repository.update_target_id(
                target_assets["Id"], user["UserId"]
            )
            user["TargetAssetsId"] = target_assets["Id"]

            # fetch the target asset for assigned to the user
            target_asset = await target_asset_repository.get_by_id(
                user["TargetAssetsId"]
            )

        # initialize pandas dataframe
        pf = pd.DataFrame()

        # list of user funds
        pf["Funds"] = [asset["FundName"] for asset in assets]

        # list of Assets
        pf["AssetType"] = [asset_type[str(asset["AssetTypeId"])] for asset in assets]

        # target asset percent
        pf["AssetPercent"] = [target_asset[asset] for asset in pf["AssetType"]]

        # Nav of each fund
        pf["NavAmount"] = [navs[fund_name]["NavAmount"] for fund_name in pf["Funds"]]

        # calculate the actual amount for each fund (actual_amount = nav * no of units)
        pf["ActualAmount"] = [
            navs[asset["FundName"]]["NavAmount"] * asset["NoOfUnits"]
            for asset in assets
        ]

        # calculate the actual percent (actual percent = (actual fund  amount / total of funds amount) * 100)
        pf["ActualPercent"] = [
            round((amount / sum(pf["ActualAmount"])) * 100, 2)
            for amount in pf["ActualAmount"]
        ]

        # fetch fund percentage as per age, amount and risk profile type.
        fund_percent = await self.fund_level_percentage(
            target_asset["Type"],
            user["SIPAmount"]
            if user["SIPAmount"] and user["Amount"]
            else user["Amount"],
        )

        # add the fund percent
        pf["FundPercent"] = [fund_percent[key] for key in pf["Funds"]]

        # calculate target percent for each fund
        pf["TargetPercent"] = [
            float(percent) * (fund_percent[key] / 100)
            for key, percent in zip(pf["Funds"], pf["AssetPercent"])
        ]

        return pf
