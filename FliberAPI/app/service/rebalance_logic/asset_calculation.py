import pandas as pd


class AssetCalculation:
    async def asset_re_balance(self, df):
        """Method to balance the assets sum to 0.

        params: df, dataframe containing asset data
        return: None
        """

        asset_to_buy = df[df.eq("Buy").any(1)]
        asset_to_sell = df[df.eq("Sell").any(1)]
        case_1 = len(asset_to_buy)
        case_2 = len(asset_to_sell)

        # if there is only two assets
        if case_1 == case_2:

            # if buy is greater than sell, subtract 1000 from buy
            if abs(sum(asset_to_buy["ToBeGiven"])) > sum(asset_to_sell["ToBeGiven"]):
                index = df.index[
                    df["Assets"] == list(asset_to_buy["Assets"])[0]
                ].tolist()
                df.at[index[0], "ToBeGiven"] = df["ToBeGiven"].loc[index[0]] + 1000

                return df["ToBeGiven"]

            # if sell is greater than buy subtract 1000 from sell
            else:
                index = df.index[
                    df["Assets"] == list(asset_to_sell["Assets"])[0]
                ].tolist()
                df.at[index[0], "ToBeGiven"] = df["ToBeGiven"].loc[index[0]] - 1000

                return df["ToBeGiven"]

        if case_1 == 1:

            # if 2 sell
            # find the lowest amount and subtract it by 1000.

            funds = df[df.eq("Sell").any(1)]
            funds = dict(
                (asset, amount)
                for asset, amount in zip(funds["Assets"], funds["ToBeGiven"])
            )
            keys = list(funds.keys())

            # if buy is greater than sell, check which fund has high value in fund
            if abs(sum(asset_to_buy["ToBeGiven"])) > sum(asset_to_sell["ToBeGiven"]):

                index_1 = df.index[df["Assets"] == keys[0]].tolist()
                index_2 = df.index[df["Assets"] == keys[1]].tolist()

                # if asset 1 percent is greater than asset 2, add 1000 from asset 2
                if (
                    df["AssetPercent"].loc[index_1[0]]
                    > df["AssetPercent"].loc[index_2[0]]
                ):
                    df.at[index_2[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_2[0]] + 1000
                    )

                # if asset 2 percent is greater than asset 1, add 1000 from asset 1
                else:
                    df.at[index_1[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_1[0]] + 1000
                    )

                return df["ToBeGiven"]

            # if asset 1 and asset 2 are equal
            if funds[keys[0]] == funds[keys[1]]:
                index_1 = df.index[df["Assets"] == keys[0]].tolist()
                index_2 = df.index[df["Assets"] == keys[1]].tolist()

                # if asset 1 percent is greater than asset 2, subtract 1000 from asset 2
                if (
                    df["AssetPercent"].loc[index_1[0]]
                    > df["AssetPercent"].loc[index_2[0]]
                ):
                    df.at[index_2[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_2[0]] - 1000
                    )

                # if asset 2 percent is greater than asset 1, subtract 1000 from asset 1
                else:
                    df.at[index_1[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_1[0]] - 1000
                    )

            # if asset 1 amount is greater than asset 2, subtract 1000 from asset 2
            elif funds[keys[0]] > funds[keys[1]]:
                index = df.index[df["Assets"] == keys[1]].tolist()
                df.at[index[0], "ToBeGiven"] = df["ToBeGiven"].loc[index[0]] - 1000

            # if asset 2 amount is greater than asset 1, subtract 1000 from asset 1
            else:
                index = df.index[df["Assets"] == keys[0]].tolist()
                df.at[index[0], "ToBeGiven"] = df["ToBeGiven"].loc[index[0]] - 1000

        else:

            # case 2:
            # if 2 buy and 1 sell

            funds = df[df.eq("Buy").any(1)]
            funds = dict(
                (asset, amount)
                for asset, amount in zip(funds["Assets"], funds["ToBeGiven"])
            )
            keys = list(funds.keys())

            # if asset amount of buy is smaller that sell amount
            if abs(sum(asset_to_buy["ToBeGiven"])) < abs(
                sum(asset_to_sell["ToBeGiven"])
            ):
                index_1 = df.index[df["Assets"] == keys[0]].tolist()
                index_2 = df.index[df["Assets"] == keys[1]].tolist()

                # if asset 1 to buy asset percent is grater than asset 2 percent add 1000 to asset 1
                if (
                    df["AssetPercent"].loc[index_1[0]]
                    > df["AssetPercent"].loc[index_2[0]]
                ):
                    df.at[index_1[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_1[0]] + 1000
                    )

                # if asset 2 to buy asset percent is grater than asset 1 percent add 1000 to asset 2
                else:
                    df.at[index_2[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_2[0]] + 1000
                    )
                return df["ToBeGiven"]

            # If B == C, find the highest asset percent and subtract the amount by 1000
            if funds[keys[0]] == funds[keys[1]]:
                index_1 = df.index[df["Assets"] == keys[0]].tolist()
                index_2 = df.index[df["Assets"] == keys[1]].tolist()
                if (
                    df["AssetPercent"].loc[index_1[0]]
                    > df["AssetPercent"].loc[index_2[0]]
                ):
                    df.at[index_1[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_1[0]] - 1000
                    )
                else:
                    df.at[index_2[0], "ToBeGiven"] = (
                        df["ToBeGiven"].loc[index_2[0]] - 1000
                    )

            # if B > C, add 1000 to B
            elif funds[keys[0]] > funds[keys[1]]:
                index = df.index[df["Assets"] == keys[0]].tolist()
                df.at[index[0], "ToBeGiven"] = df["ToBeGiven"].loc[index[0]] + 1000

            # if C > B, add 1000 to C
            else:
                index = df.index[df["Assets"] == keys[1]].tolist()
                df.at[index[0], "ToBeGiven"] = df["ToBeGiven"].loc[index[0]] + 1000

        return df["ToBeGiven"]

    async def asset_calculation(self, dataframe, sip_account=False):
        """Method to calculate the asset level amount

        params: dataframe
        return: dataframe
        """
        df = dataframe

        total_actual_amount = sum(df["ActualAmount"])

        asset_types = set(df["AssetType"])
        bdf = pd.DataFrame()
        bdf["Assets"] = list(asset_types)
        target_percent = {
            key: value for key, value in zip(df["AssetType"], df["AssetPercent"])
        }

        target_total = {}
        balance = {}
        target_asset_amount = {}

        bdf["TargetPercent"] = [float(target_percent[asset]) for asset in bdf["Assets"]]
        for asset in asset_types:
            target_asset_amount[asset] = round(
                total_actual_amount * (float(target_percent[asset]) / 100), 4
            )
            target_total[asset] = sum(df[df.eq(asset).any(1)]["ActualAmount"])
            balance[asset] = round(target_total[asset] - target_asset_amount[asset], -3)

        bdf["AssetAmount"] = [target_total[asset] for asset in bdf["Assets"]]
        bdf["AssetPercent"] = [
            round(amount / sum(bdf["AssetAmount"]) * 100, 2)
            for amount in bdf["AssetAmount"]
        ]
        bdf["TargetAmount"] = [target_asset_amount[asset] for asset in bdf["Assets"]]

        if sip_account:
            return bdf

        bdf["ToBeGiven"] = [balance[asset] for asset in bdf["Assets"]]
        bdf["Action"] = [
            "Sell" if balance[asset] > 0 else "Buy" for asset in bdf["Assets"]
        ]

        while sum(bdf["ToBeGiven"]):
            bdf["ToBeGiven"] = await self.asset_re_balance(
                bdf[["Assets", "Action", "AssetAmount", "ToBeGiven", "AssetPercent"]]
            )

        bdf["Amount"] = [
            abs(asset_amount - amount)
            for asset_amount, amount in zip(bdf["TargetAmount"], bdf["ToBeGiven"])
        ]
        bdf["BalancedPercent"] = [
            amount / sum(bdf["Amount"]) * 100 for amount in bdf["Amount"]
        ]

        return bdf[["Assets", "ToBeGiven"]]
