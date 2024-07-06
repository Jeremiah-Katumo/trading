
import pandas as pd
from lumibot.backtesting import BacktestingBroker, PandasDataBacktesting
from lumibot.entities import Asset, Data
from lumibot.strategies import Strategy
from lumibot.traders import Trader
import yfinance as yf
from lumibot.entities import Asset
from lumibot.backtesting import (YahooDataBacktesting, BacktestingBroker, 
                                 PandasDataBacktesting, PolygonDataBacktesting)
import pandas as pd
from lumibot.entities import Data

# Download minute data for the last 5 days for AAPL
data = yf.download("AAPL", period="5d", interval="1m")

# Save the data to a CSV file
data.to_csv("AAPL.csv")

# A simple strategy that buys SPY on the first day
class MyStrategy(Strategy):
    def on_trading_iteration(self):
        if self.first_iteration:
            order = self.create_order("AAPL", 100, "buy")
            self.submit_order(order)


# Read the data from the CSV file (in this example you must have a file named "AAPL.csv"
# in a folder named "data" in the same directory as this script)
df = pd.read_csv("AAPL.csv")
asset = Asset(
    symbol="AAPL",
    asset_type=Asset.AssetType.STOCK,
)
pandas_data = {}
pandas_data[asset] = Data(
    asset,
    df,
    timestep="minute",
)

# Pick the date range you want to backtest
backtesting_start = pandas_data[asset].datetime_start
backtesting_end = pandas_data[asset].datetime_end

# Run the backtesting
trader = Trader(backtest=True)
data_source = PandasDataBacktesting(
    pandas_data=pandas_data,
    datetime_start=backtesting_start,
    datetime_end=backtesting_end,
)
broker = BacktestingBroker(data_source)
strat = MyStrategy(
    broker=broker,
    budget=100000,
)
trader.add_strategy(strat)
trader.run_all()
