
# Run a strategy on Alpaca
from lumibot.strategies import Strategy
from lumibot.brokers import Alpaca
from lumibot.traders import Trader
from lumibot.entities import Asset

ALPACA_CONFIG = {
    # Put your own Alpaca key here:
    "API_KEY": "YOUR_API_KEY",
    # Put your own Alpaca secret here:
    "API_SECRET": "YOUR_API_SECRET",
    # If you want to go live, you must change this
    "ENDPOINT": "https://paper-api.alpaca.markets",
}

class AlpacaStrategy(Strategy):
    def on_trading_interation(self):
        if self.broker.is_market_open():
            self.create_order(
                asset=Asset(symbol="AAPL"),
                quantity=1,
                order_type="market",
                side="buy",
            )

alpaca = Alpaca(ALPACA_CONFIG)
strategy = AlpacaStrategy(broker=alpaca)
trader = Trader()
trader.add_strategy(strategy)
trader.run()
