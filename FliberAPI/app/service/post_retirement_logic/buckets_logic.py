import numpy as np
import numpy_financial as npf
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.bucket import BucketRepository


def npv(rate, values):
    values = np.asarray(values)
    return (values / (1 + rate) ** np.arange(1, len(values) + 1)).sum(axis=0)


class Buckets:

    def __init__(self, db_session: AsyncSession) -> None:
        self._db_session: AsyncSession = db_session

    async def calculate_bucket(self, start, end, rate, yr=0, net_cf=None):

        if end == 0:
            end = ""

        try:
            b2_val = (
                    npv(rate, net_cf.loc[start:end]) + net_cf.loc[start - 1]
            )

            pv = npf.pv(rate, yr, 0, b2_val, 1)
        except KeyError:
            pv = 0

        return pv

    async def generate_bucket(self, corpus_amount, data):

        bucket_rate = BucketRepository(self._db_session)

        for i, net_amount in enumerate(data["Normalized CF"]):

            opening_balance = (
                corpus_amount + net_amount
                if net_amount
                else corpus_amount + data["Net CF"][i]
            )
            data.loc[i, "Opening Balance"] = round(opening_balance, 4)

            brate = await bucket_rate.get_all_rate()
            brate.pop(0)

            gr = [r[0] for r in brate]
            gi = [y[1] for y in brate if y[1] > 0]

            index = len(brate)

            yr = gi.pop(0) + 1
            r = gr.pop(0) / 100

            yr = int(yr)

            if opening_balance > 0:
                b1_npv = abs(
                    round(npv(r, data["Normalized CF"].iloc[i + 1: i + yr]), 4)
                )
                if opening_balance > b1_npv:
                    balance = abs(
                        round(npv(r, data["Normalized CF"].iloc[i + 1: i + yr]), 4)
                    )
                else:
                    balance = opening_balance
            else:
                balance = 0

            total_g = abs(balance * r)
            data.loc[i, f"Bucket NPV 1"] = 0
            data.loc[i, f"Investment 1"] = round(balance, 4)
            data.loc[i, f"Growth 1"] = round(total_g, 4)
            for k, key in enumerate(gi):
                start = yr + i
                end = key - 1

                interest_rate = gr.pop(0) / 100

                pv = await self.calculate_bucket(
                    start=start + 1, end=start + end, rate=interest_rate, yr=yr, net_cf=data["Normalized CF"]
                )

                data.loc[i, f"Bucket NPV {k + 2}"] = round(abs(pv), 4)
                if balance == opening_balance or opening_balance <= 0:
                    iv = 0
                    data.loc[i, f"Investment {k + 2}"] = round(iv, 4)

                elif opening_balance - balance > pv:
                    iv = pv
                    data.loc[i, f"Investment {k + 2}"] = round(iv, 4)
                else:
                    bal = opening_balance - balance
                    iv = bal if bal > 0 else 0
                    data.loc[i, f"Investment {k + 2}"] = round(iv, 4)

                balance += abs(round(iv, 4))

                grw = iv * interest_rate
                total_g += abs(grw)
                data.loc[i, f"Growth {k + 2}"] = round(abs(grw), 4)
                yr = start + end

            interest_rate = gr.pop(0) / 100
            balance = (
                0 if balance > opening_balance else (opening_balance - balance)
            )
            data.loc[i, f"Bucket NPV {index}"] = round(0)
            data.loc[i, f"Investment {index}"] = round(balance, 4)

            grw = balance * interest_rate
            total_g += grw
            data.loc[i, f"Growth {index}"] = round(grw, 4)
            closing_balance = opening_balance + total_g
            corpus_amount = closing_balance
            data.loc[i, "Port Growth"] = round(total_g, 4)
            data.loc[i, "Closing Balance"] = round(closing_balance, 4)

        return data
