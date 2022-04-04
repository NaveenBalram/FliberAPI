from app.service.rebalance_logic.asset_calculation import AssetCalculation


class SIPCalculation:
    async def smart_sip_rebalance(self, df, assets):

        for asset in assets:

            data = df[df.eq(asset).any(1)].sort_values(by=["Drift"])

            negative_indexes = data.index[data["Drift"] < 0].tolist()
            negative_indexes = sorted(negative_indexes)
            alloted_amount = set(df[df.eq(asset).any(1)]["AssetAmount"])
            alloted_amount = alloted_amount.pop()
            received_amount = alloted_amount

            if len(negative_indexes) == 1 and len(data) == 1:
                index = negative_indexes[0]
                df.at[index, "ActualAmount"] = (
                        df["ActualAmount"].loc[index] + alloted_amount
                )
                df.at[index, "Required"] = alloted_amount

            else:

                for index in negative_indexes:

                    required = df["Required"].loc[index]

                    if alloted_amount > required:
                        alloted_amount = alloted_amount - required
                        df.at[index, "ActualAmount"] = (
                                df["ActualAmount"].loc[index] + required
                        )
                        df.at[index, "Required"] = required
                    else:

                        df.at[index, "ActualAmount"] = (
                                df["ActualAmount"].loc[index] + alloted_amount
                        )
                        df.at[index, "Required"] = alloted_amount
                        alloted_amount = 0

            if alloted_amount:
                positive_indexes = data.index[data["Drift"] >= 0].tolist()

                if len(positive_indexes) == 1 and len(data) == 1:
                    index = positive_indexes[0]
                    df.at[index, "ActualAmount"] = (
                            df["ActualAmount"].loc[index] + alloted_amount
                    )
                    df.at[index, "Required"] = alloted_amount

                else:
                    total_percent = sum(data[data["Drift"] >= 0]["FundPercent"])
                    for index in positive_indexes:
                        required = round(
                            alloted_amount
                            * (data["FundPercent"].loc[index] / total_percent),
                            -3,
                        )
                        df.at[index, "Required"] = required
                        df.at[index, "ActualAmount"] = (
                                df["ActualAmount"].loc[index] + required
                        )

                    while 1:

                        if sum(df[df.eq(asset).any(1)]["Required"]) > received_amount:
                            index = data["Drift"].idxmax()
                            df.at[index, "Required"] = df["Required"].loc[index] - 1000
                            df.at[index, "ActualAmount"] = (
                                    df["ActualAmount"].loc[index] - 1000
                            )

                        elif sum(df[df.eq(asset).any(1)]["Required"]) < received_amount:
                            index = data["Drift"].idxmax()
                            df.at[index, "Required"] = df["Required"].loc[index] + 1000
                            df.at[index, "ActualAmount"] = (
                                    df["ActualAmount"].loc[index] + 1000
                            )
                        else:
                            break

        data = dict((name, amount) for name, amount in zip(df["Funds"], df["Required"]))
        return data

    async def sip_rebalance(self, dataframe, sip_amount, smart_sip=False):
        df = dataframe

        df["Drift"] = [
            ap - tp for ap, tp in zip(df["ActualPercent"], df["TargetPercent"])
        ]

        assets = set(df["AssetType"])
        fund_total = sum(df["ActualAmount"]) + sip_amount

        df["TargetAmount"] = [
            fund_total * (percent / 100) for percent in df["TargetPercent"]
        ]
        df["Required"] = [
            abs(round(av - tv, -3))
            for av, tv in zip(df["ActualAmount"], df["TargetAmount"])
        ]

        if smart_sip:
            return await self.smart_sip_rebalance(df, assets)

        df["Required"] = [0 for i in df["Funds"]]

        for asset in assets:
            data = df[df.eq(asset).any(1)]

            alloted_amount = set(df[df.eq(asset).any(1)]["AssetAmount"])
            alloted_amount = alloted_amount.pop()
            received_amount = set(df[df.eq(asset).any(1)]["AssetAmount"])
            received_amount = received_amount.pop()

            if alloted_amount == 1000:
                index = data["Drift"].idxmax()
                df.at[index, "Required"] = alloted_amount
                df.at[index, "ActualAmount"] = (
                        df["ActualAmount"].loc[index] + alloted_amount
                )

            else:
                indexes = data.index[data["AssetType"] == asset].tolist()

                for index in indexes:
                    amount = round(
                        alloted_amount * (df["FundPercent"].loc[index] / 100), -3
                    )
                    df.at[index, "Required"] = amount
                    df.at[index, "ActualAmount"] = (
                            df["ActualAmount"].loc[index] + amount
                    )

                while 1:

                    if sum(df[df["AssetType"] == asset]["Required"]) > received_amount:
                        index = data["Drift"].idxmax()
                        df.at[index, "Required"] = df["Required"].loc[index] - 1000
                        df.at[index, "ActualAmount"] = (
                                df["ActualAmount"].loc[index] - 1000
                        )

                    elif (
                            sum(df[df["AssetType"] == asset]["Required"]) < received_amount
                    ):
                        index = data["Drift"].idxmax()
                        df.at[index, "Required"] = df["Required"].loc[index] + 1000
                        df.at[index, "ActualAmount"] = (
                                df["ActualAmount"].loc[index] + 1000
                        )
                    else:
                        break

        required = dict(
            (fund, amount)
            for fund, amount in zip(df["Funds"], df["Required"])
            if amount > 0
        )

        return required

    async def sip_calculation(self, bdf, sip_amount):

        ac = AssetCalculation()
        bdf = await ac.asset_calculation(bdf, True)

        bdf["Drift"] = [
            float(ap) - float(tp)
            for ap, tp in zip(bdf["AssetPercent"], bdf["TargetPercent"])
        ]

        asset_sum = sum(bdf["AssetAmount"]) + sip_amount

        drifts = bdf.sort_values(by=["Drift"])
        negative_index = drifts.index[drifts["Drift"] < 0].tolist()

        for index in negative_index:

            required = (asset_sum * (bdf["TargetPercent"].loc[index] / 100)) - bdf[
                "AssetAmount"
            ].loc[index]
            required = round(required, -3)

            if sip_amount > required:
                sip_amount = sip_amount - required
                bdf.at[index, "AssetAmount"] = bdf["AssetAmount"].loc[index] + required
                bdf.at[index, "Required"] = required
            else:
                bdf.at[index, "AssetAmount"] = (
                        bdf["AssetAmount"].loc[index] + sip_amount
                )
                bdf.at[index, "Required"] = sip_amount
                sip_amount = 0

        positive_index = drifts.index[drifts["Drift"] >= 0].tolist()
        if sip_amount:
            positive_index = drifts.index[drifts["Drift"] >= 0].tolist()
            target_percent = sum(drifts[drifts["Drift"] >= 0]["TargetPercent"])

            if len(positive_index) == 1:
                index = positive_index[0]
                bdf.at[index, "Required"] = sip_amount
                bdf.at[index, "AssetAmount"] = (
                        bdf["AssetAmount"].loc[index] + sip_amount
                )

            else:

                for index in positive_index:
                    required = round(
                        (sip_amount * bdf["TargetPercent"].loc[index]) / target_percent,
                        -3,
                    )

                    bdf.at[index, "Required"] = required
                    bdf.at[index, "AssetAmount"] = (
                            bdf["AssetAmount"].loc[index] + required
                    )
        else:
            for index in positive_index:
                bdf.at[index, "Required"] = 0

        return bdf[["Assets", "AssetAmount", "Required"]]
