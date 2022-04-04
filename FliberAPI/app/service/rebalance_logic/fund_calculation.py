class FundCalculation:
    async def fund_calculation(self, dataframe):
        """Method to do a fund level calculation for rebalancing

        param: dataframe, holds portfolio data
        return: dict, holds fund data to buy or sell

        """
        df = dataframe

        amount = sum(df["ActualAmount"])
        df["Deficit"] = [
            round(actual - target, 2)
            for actual, target in zip(df["ActualPercent"], df["TargetPercent"])
        ]
        df["TargetAmount"] = [amount * (value / 100) for value in df["TargetPercent"]]

        df["Required"] = [
            round(av - tv, -3) for av, tv in zip(df["ActualAmount"], df["TargetAmount"])
        ]

        asset_amount = {
            key: value for key, value in zip(df["AssetType"], df["AssetAmount"])
        }

        items = {"Buy": [], "Sell": []}

        for asset, amount in asset_amount.items():
            if abs(amount) == 0:
                continue

            funds = df.loc[df["AssetType"] == asset]

            # sort to get -ve drifts in ascending order
            if amount < 0:
                sorted_deficit = sorted(funds["Deficit"])

            # sort to get +ve drift in descending order
            else:
                sorted_deficit = sorted(funds["Deficit"], reverse=True)

            for value in sorted_deficit:

                index = funds.index[funds["Deficit"] == value].tolist()

                if value < 0:
                    asset_type = "Buy"
                else:
                    asset_type = "Sell"

                if abs(amount) == 1000:
                    items[asset_type].append(
                        {asset: {funds["Funds"].loc[index[0]]: abs(amount)}}
                    )

                    df.at[index[0], "ActualAmount"] = (
                            df["ActualAmount"].iloc[index[0]]
                            - df["Required"].iloc[index[0]]
                    )
                    df.at[index[0], "Required"] = 0
                    amount = 0

                elif abs(amount) > abs(df["Required"].iloc[index[0]]):
                    items[asset_type].append(
                        {
                            asset: {
                                funds["Funds"].loc[index[0]]: abs(
                                    df["Required"].iloc[index[0]]
                                )
                            }
                        }
                    )

                    amount = amount - df["Required"].iloc[index[0]]
                    df.at[index[0], "ActualAmount"] = (
                            df["ActualAmount"].iloc[index[0]]
                            - df["Required"].iloc[index[0]]
                    )
                    df.at[index[0], "Required"] = 0

                else:

                    items[asset_type].append(
                        {asset: {funds["Funds"].loc[index[0]]: abs(amount)}}
                    )
                    df.at[index[0], "Required"] = df["Required"].iloc[index[0]] - amount
                    df.at[index[0], "ActualAmount"] = (
                            df["ActualAmount"].iloc[index[0]] - amount
                    )
                    amount = 0

                if amount == 0:
                    break

        return items
