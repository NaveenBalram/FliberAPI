from sqlalchemy.ext.asyncio import AsyncSession

from app.service.post_retirement_logic.buckets_logic import Buckets
from app.service.post_retirement_logic.goals_logic import Goals
from app.service.post_retirement_logic.income_logic import Income


class CashLadder:

    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def generate_cash_ladder(self, user_goals, uer_income, r_age, e_age, data, corpus):
        goal_data = Goals(self._db_session)
        income_data = Income(self._db_session)
        buckets = Buckets(self._db_session)

        goal_names = await goal_data.generate_goals(user_goals, r_age, e_age, data)
        income_names = await income_data.generate_income(uer_income, r_age, e_age, data)

        data["Net CF"] = (
            data[income_names].sum(axis=1).sub(data[goal_names].sum(axis=1), axis=0)
        )

        data["Normalized CF"] = [cf if cf < 0 else 0 for cf in data["Net CF"]]

        data = await buckets.generate_bucket(corpus, data)

        return data