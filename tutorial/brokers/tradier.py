
from lumibot.brokers import Tradier
from lumibot.traders import Trader
from lumibot.strategies import Strategy

TRADIER_CONFIG = {
    "ACCESS_TOKEN": "your_access_token",
    "ACCOUNT_NUMBER": "your_account_number",
    "PAPER": True,
}

class MyStrategy(Strategy):
    def on_trading_iteration(self):
        # Buy 1 share of AAPL if the price is less than $100
        price = self.get_last_price("AAPL")
        self.log_message(f"AAPL price: {price}")

broker = Tradier(config=TRADIER_CONFIG)
strategy = MyStrategy(broker=broker)
trader = Trader()
trader.add_strategy(strategy)
strategy_executors = trader.run_all()