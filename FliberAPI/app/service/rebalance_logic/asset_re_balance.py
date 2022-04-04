import logging
import random
from datetime import datetime
from uuid import UUID

import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.asset_type import AssetTypeRepository
from app.db.repositories.assets_limit import AssetsLimitRepository
from app.db.repositories.funds_category import FundsCategoryRepository
from app.db.repositories.morning_star_navs import MorningStarNavsRepository
from app.db.repositories.re_balance import ReBalanceRepository
from app.db.repositories.target_assets import TargetAssetsRepository
from app.db.repositories.user import UserRepository
from app.db.repositories.user_assets import UserAssetsRepository
from app.db.repositories.users_re_balance_sheet import UsersReBalanceSheetRepository
from app.models.schema.re_balance import (
    OutReBalanceSchema,
    ReBalanceSchema,
    ReBalanceSchemaBase,
)


class AssetReBalance:
    def __init__(self, payload, db_session: AsyncSession) -> None:
        """constructor to assign database session

        params: db_session, connection to database
        return: None
        """
        self._db_session: AsyncSession = db_session
        self._payload = payload
