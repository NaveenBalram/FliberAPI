import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.assets_limit import AssetsLimitRepository
from app.db.repositories.target_assets import TargetAssetsRepository
from app.db.repositories.users_re_balance_sheet import UsersReBalanceSheetRepository
from app.service.rebalance_logic.portfolio import Portfolio


class ReBalanceRequired:
    def __init__(self, dataframe, db_session: AsyncSession):
        self._under_watch = False
        self._trigger = False
        self._pd = dataframe
        self._db_session = db_session
        self.portfolio = Portfolio(self._db_session)

    async def get_asset_limit(self, asset_type):
        """Method to get the asset limit."""

        asset_limits = AssetsLimitRepository(self._db_session)
        asset_limits = await asset_limits.get_all()
        return dict((asset_type[str(x["AssetTypeId"])], x) for x in asset_limits)

    async def get_target_assets(self, target_id):
        """Method to fetch the target assets"""

        target_assets = TargetAssetsRepository(self._db_session)
        return await target_assets.get_by_id(target_id)

    async def check_rebalance_required(self, user):
        """Method to check is rebalance required for the user portfolio"""

        total_amount = sum(self._pd["ActualAmount"])

        assets = await self.portfolio.get_asset_type()
        target_asset = await self.get_target_assets(user["TargetAssetsId"])
        asset_limits = await self.get_asset_limit(assets)

        for key, asset in assets.items():

            cross_limit = asset_limits[asset]["AssetCrossLimit"]
            bound = round(
                (
                        sum(self._pd[self._pd.eq(asset).any(1)]["ActualAmount"])
                        / total_amount
                )
                * 100,
                4,
            )

            lower_max_limit = int(target_asset[asset]) - (
                    asset_limits[asset]["AssetLowerLimit"] + cross_limit
            )

            upper_max_limit = (
                    int(target_asset[asset])
                    + asset_limits[asset]["AssetUpperLimit"]
                    + cross_limit
            )

            if bound < lower_max_limit or bound > upper_max_limit:
                self._trigger = True
                break

            lower_limit = lower_max_limit - cross_limit
            upper_limit = upper_max_limit - cross_limit

            if bound < lower_limit or bound > upper_limit:
                self._under_watch = True

        user_balance_repository = UsersReBalanceSheetRepository(self._db_session)

        if self._under_watch:

            watch_day = user["WatchDays"] + 1
            await user_balance_repository.update_watch_day(user["UserId"], watch_day, datetime.datetime.now())
            await user_balance_repository.set_status(user["UserId"], "UnderWatch", datetime.datetime.now())

            if watch_day > 7:
                await user_balance_repository.set_status(user["UserId"], "Initiated", datetime.datetime.now())
                await user_balance_repository.update_watch_day(user["UserId"], 0, datetime.datetime.now())
                self._trigger = True
        else:
            await user_balance_repository.update_watch_day(user["UserId"], 0, datetime.datetime.now())
            if not self._trigger:
                await user_balance_repository.set_status(user["UserId"], "Completed", datetime.datetime.now())

        if self._trigger:
            return self._trigger
        elif self._under_watch:
            return "Rebalance"

        return self._trigger
