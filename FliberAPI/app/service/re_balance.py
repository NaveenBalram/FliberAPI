import datetime
import logging
from uuid import UUID

from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.users_re_balance_sheet import UsersReBalanceSheetRepository
from app.models.schema.re_balance import (
    OutReBalanceSchema,
    ReBalanceSchema,
    ReBalanceSchemaBase,
)
from app.models.schema.re_balance import SIPReBalance
from app.service.rebalance_logic.asset_calculation import AssetCalculation
from app.service.rebalance_logic.check_rebalance import ReBalanceRequired
from app.service.rebalance_logic.fund_calculation import FundCalculation
from app.service.rebalance_logic.portfolio import Portfolio
from app.service.rebalance_logic.sip_calculation import SIPCalculation

router = APIRouter()

logger = logging.getLogger(__name__)


class ReBalance:
    def __init__(self, payload, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._re_balance_repository = ReBalanceRepository(self._db_session)

    async def get_portfolio(self):
        """Method to generate daily portfolio for a user and check whether rebalancing is required."""

        # initialize repositories
        user_balance_repository = UsersReBalanceSheetRepository(self._db_session)

        # get all user data except whose transaction and rebalance status is 'InProgress'
        users = await user_balance_repository.get_all_by_status(None)

        # for each user generate portfolio and check if rebalance is required.
        for user in users:
            portfolio = Portfolio(self._db_session)
            pd = await portfolio.generate_portfolio(user["UserId"])

            re_balance = ReBalanceRequired(pd, self._db_session)
            trigger = await re_balance.check_rebalance_required(user)

            assets = {}
            rebalance = {}
            if trigger is True:
                ac = AssetCalculation()
                assets = await ac.asset_calculation(pd)
                assets = dict(
                    (asset, amount)
                    for asset, amount in zip(assets["Assets"], assets["ToBeGiven"])
                )
                pd["AssetAmount"] = [assets[asset] for asset in pd["AssetType"]]

                fc = FundCalculation()
                rebalance = await fc.fund_calculation(pd)

                await user_balance_repository.update_watch_day(user["UserId"], 0, datetime.datetime.now())

                if assets and rebalance:

                    await user_balance_repository.set_status(
                        user["UserId"], "Initiated", datetime.datetime.now()
                    )
                    return {"Assets": assets, "Funds": rebalance}

                elif assets:

                    await user_balance_repository.set_status(
                        user["UserId"], "Completed", datetime.datetime.now()
                    )
                    return "Balanced Out!"
                else:

                    await user_balance_repository.set_status(
                        user["UserId"], "Completed", datetime.datetime.now()
                    )
                    return "Re balance not required!"
            elif trigger == "Rebalance":
                return "Portfolio is under watch!"

            return "Re balance not required!"

    async def get_sip_portfolio(self, smart_sip=False):

        # initialize repositories
        user_balance_repository = UsersReBalanceSheetRepository(self._db_session)

        # get all user data except whose transaction and rebalance status is 'InProgress'
        users = await user_balance_repository.get_all_by_status(None)

        # for each user generate portfolio and check if rebalance is required.
        for user in users:
            portfolio = Portfolio(self._db_session)
            pd = await portfolio.generate_portfolio(user["UserId"])

            sipc = SIPCalculation()
            assets = await sipc.sip_calculation(pd, user["SIPAmount"])
            asset_data = dict(
                (asset, amount)
                for asset, amount in zip(assets["Assets"], assets["Required"])
                if amount > 0
            )

            if asset_data:
                assets = dict(
                    (asset, amount)
                    for asset, amount in zip(assets["Assets"], assets["Required"])
                )

                pd["AssetAmount"] = [assets[asset] for asset in pd["AssetType"]]
            else:
                return "Asset level returned empty"

            rebalance = await sipc.sip_rebalance(pd, user["SIPAmount"], smart_sip)
            await user_balance_repository.update_watch_day(user["UserId"], 0, datetime.datetime.now())

            if assets and rebalance:
                await user_balance_repository.set_status(user["UserId"], "Initiated", datetime.datetime.now())
                return {"Assets": assets, "Funds": rebalance}
            elif assets:
                return "Balanced Out!"


class ReBalanceService:
    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session
        self._re_balance_repository = ReBalanceRepository(self._db_session)

    async def create(self, payload: ReBalanceSchemaBase):
        if payload.Amount:
            user_re_balance = UsersReBalanceSheetRepository(self._db_session)
            await user_re_balance.update_rebalance_sheet(payload, payload.UserId)

        rb = ReBalance(payload, self._db_session)
        return await rb.get_portfolio()

    async def sip_re_balance(self, payload: SIPReBalance):
        if payload.Amount or payload.SIPAmount:
            if payload.Amount > 0 and payload.Amount < 50000:
                return "Minimun intial amount should be 50000"
            if payload.SIPAmount > 0 and payload.SIPAmount < 5000:
                return "SIP amount should be grater then 4999."
            if payload.SmartSip:
                if payload.SIPAmount < 20000:
                    return "Smart SIP amount should greater than or equal to 20000."

            user_re_balance = UsersReBalanceSheetRepository(self._db_session)
            await user_re_balance.update_sip_rebalance_sheet(payload, payload.UserId)
            srb = ReBalance(payload, self._db_session)
            return await srb.get_sip_portfolio(payload.SmartSip)
        else:
            srb = ReBalance(payload, self._db_session)
            return await srb.get_sip_portfolio(payload.SmartSip)

    async def get_by_id(self, uuid: UUID) -> OutReBalanceSchema:
        re_balance = await self._re_balance_repository.get_by_id(uuid)
        return re_balance

    async def get_all(self):
        re_balance = await self._re_balance_repository.get_all()
        return re_balance

    async def delete(self, uuid: UUID):
        await self._re_balance_repository.delete(uuid)

    async def update(self, payload: ReBalanceSchema):
        await self._re_balance_repository.update(payload)
