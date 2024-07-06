
from datetime import datetime
from lumibot.traders import Trader
from lumibot.brokers import Alpaca
from lumibot.strategies.strategy import Strategy
from lumibot.backtesting import YahooDataBacktesting, PandasDataBacktesting, PolygonDataBacktesting
from lumibot.entities import TradingFee

# Will return the last price for a crypto asset
def on_trading_iteration(self):
    base = Asset(symbol="BTC", asset_type="crypto")
    quote = Asset(symbol="USD", asset_type="forex")
    last_price = self.get_last_price(base, quote)

    # Will return the last price for the assets
    assets = ["SPY", "TLT"]
    last_prices = self.get_last_prices(assets)