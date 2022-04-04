import logging
import os
from enum import Enum
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, PostgresDsn

logger = logging.getLogger(__name__)


class SendGridKey:
    KEY = "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"


class CashFreeKeys:
    KEY_ID = "109422ebe766ad587283cdc233224901"
    KEY_SECRET = "cd1279c250f725c717974fb52679707e80d57cbb"


class EnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    LOCAL = "local"


class FliberUrl:
    url = "http://fliberdevapi.azurewebsites.net/"


class GlobalConfig(BaseSettings):
    TITLE: str = "Fliber"
    DESCRIPTION: str = "This is a Fliber API project"

    ENVIRONMENT: EnvironmentEnum
    DEBUG: bool = False
    TESTING: bool = False
    TIMEZONE: str = "UTC"

    # DATABASE_URL: Optional[
    #     PostgresDsn
    # ] = "postgresql://postgres:postgres@127.0.0.1:5432/postgres"
    DATABASE_URL: Optional[
        PostgresDsn
    ] = "postgresql://fliberadmin@fliber-dev:nIi6TUcBtS@fliber-dev.postgres.database.azure.com:5432/postgres1"
    DB_ECHO_LOG: bool = False

    TEST_DATABASE_URL: Optional[
        PostgresDsn
    ] = "postgresql://fliberadmin@fliber-dev:nIi6TUcBtS@fliber-dev.postgres.database.azure.com:5432/TestDB"
    TEST_DB_ECHO_LOG: bool = False

    @property
    def async_database_url(self) -> Optional[str]:

        return (
            self.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            if self.DATABASE_URL
            else self.DATABASE_URL
        )

    @property
    def test_async_database_url(self, ) -> Optional[str]:

        return (
            self.TEST_DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")
            if self.TEST_DATABASE_URL
            else self.TEST_DATABASE_URL
        )


    # Api V1 prefix
    API_V1_STR = "/v1"

    class Config:
        case_sensitive = True


class LocalConfig(GlobalConfig):
    """Local configurations."""

    DEBUG: bool = True
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.LOCAL


class ProdConfig(GlobalConfig):
    """Production configurations."""

    DEBUG: bool = False
    ENVIRONMENT: EnvironmentEnum = EnvironmentEnum.PRODUCTION


class FactoryConfig:
    def __init__(self, environment: Optional[str]):
        self.environment = environment

    def __call__(self) -> GlobalConfig:
        if self.environment == EnvironmentEnum.LOCAL.value:
            return LocalConfig()
        return ProdConfig()


# class GetConfig:
#
#     @classmethod
#     def rrcaldata(cls):
#         rrcaldata = dict(RORforEPFOandGS=15, EquityRORforNPSandMLI=15,
#                          DebtORforNPSandMLI=8, InflationRate=5, RateofReturn=8, life_exp=85, retirement_age=60)
#         return rrcaldata
#
#     @classmethod
#     def pre_retirement_data(cls):
#         pre_retirement_data = dict(retirement_age=58, inflation=6, life_exp=90, calulationlimit=100,
#                                    health_care_inflation=12, growthofIncomerate=5, vacation_inflation=7.5,
#                                    discounting_rate=7, asis=0, luxury=10, modest=-10)
#         return pre_retirement_data
#
#     @classmethod
#     def sustainabilityScore(cls):
#         sustainabilityScore = dict(retirement_age=60, inflation=6, life_exp=85, rateofReturn=10,
#                                    health_care_inflation=10)
#         return sustainabilityScore


@lru_cache()
def get_configuration() -> GlobalConfig:
    return FactoryConfig(os.environ.get("ENVIRONMENT"))()


settings = get_configuration()
