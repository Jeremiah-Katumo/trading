
from datetime import datetime
from lumibot.traders import Trader
from lumibot.brokers import Alpaca
from lumibot.strategies.strategy import Strategy
from lumibot.backtesting import (YahooDataBacktesting, BacktestingBroker, 
                                 PandasDataBacktesting, PolygonDataBacktesting)
from lumibot.entities import TradingFee
import yappi
from dotenv import load_dotenv
import os

load_dotenv()

# Configure your API Keys
ALPACA_CONFIG = {
    "API_KEY": os.getenv("ALPACA_API_KEY"),
    "API_SECRET": os.getenv("ALPACA_SECRET_KEY"),
    "PAPER": True   # set to False to use a live account
}

# Create a strategy class
class MyStrategy(Strategy):
    # Custom parameter
    parameters = {
        "symbol": ["SPY", "AAPL"],
        "quantity": 1,
        "side": "buy"
    }

    def initialize(self, symbol: str = ["SPY", "AAPL"], minutes_before_closing: int = 5, max_bars: int = 100):
        # Will make on_trading_iteration() run every 180 minutes
        self.symbol = symbol
        self.sleeptime = "180M"
        self.last_trade = None
        self.minutes_before_closing = minutes_before_closing
        self.max_bars = max_bars

    def on_trading_iteration(self):
        # symbol = [] # self.symbol # self.parameters["symbol"]
        orders = []
        quantity = self.parameters["quantity"]
        side = self.parameters["side"]

        for sym in self.symbol:
            order = self.create_order(symbol=sym, quantity=quantity, side=side)
            orders.append(order)
            
        self.submit_orders(orders)     # self.submit_order(order)
        # self.cancel_orders(orders)   # self.cancel_order(order)

        # Check condition to sell asset (example condition: if we own more than 50 shares)
        for sym in self.symbol:
            position = self.positions.get(sym, None)
            if position and position.quantity > 50:
                selling_order = self.get_selling_order(sym, 50)
                self.submit_order(selling_order)

            total = self.get_asset_potential_total(sym)
            self.log_message(f"Symbol: {sym}, Total potential: {total}")

        all_orders = self.get_orders()
        for order in all_orders:
            if order.status == "filled":
                self.log_message(f"Order {order.id} filled")
        # Example: Cancel all open orders
        open_orders = [order for order in all_orders if order.status == 'open']
        if open_orders:
            self.cancel_orders(open_orders)

    # def trace_stats lifecycle method that will be executed after on_trading_iteration.
    # context is a dict containing the result of locals() of on_trading_iteration() at the end of its execution.
    # use this method to dump stats.
    def trace_stats(self, context: dict, snapshot_before: dict):
        self.log_message("Trace stats")
        self.log_message(f"Context: {context}")
        self.log_message(f"Snapshot before: {snapshot_before}")
        return {
            "portfolio_value": self.portfolio_value,
            "cash": self.cash,
            # "order_book": self.order_book,
            # "portfolio_value_history": self.portfolio_value_history,
            # "trade_history": self.trade_history,
            # "total_trades": self.total_trades,
        }
        # return super().trace_stats(context, snapshot_before)

    # def before_market_opens lifecycle method is executed each day before market opens. If the strategy is first 
    # run when the market is already open, this method will be skipped the first day. Use this 
    # lifecycle methods to execute business logic before starting trading like canceling all open orders.
    def before_market_opens(self):
        bars_list = self.get_historical_prices_for_assets(assets=self.symbol, length=1, timestep="day")
        for asset_bars in bars_list:
            self.log_message(asset_bars.df)

    # def before_starting_trading lifecycle method is used to reinitialize variables for day trading like resetting the list of blacklisted shares.
    def before_starting_trading(self):
        for sym in self.symbol:
            self.get_historical_prices(sym, 1, "day")    # data management
        # return super().before_starting_trading()

    # def before_market_closes This lifecycle method is executed self.minutes_before_closing minutes before the market closes. 
    # Use this lifecycle method to execute business logic like selling shares and closing open orders.
    def before_market_closes(self):
        self.sell_all()
        # self.cancel_open_orders()
        # return super().before_market_closes()

    # def after_market_closes is executed right after the market closes.
    def after_market_closes(self):
        self.log_message("Market closed")
        self.log_message(f"The total value of our portfolio is {self.portfolio_value}")
        self.log_message(f"The amount of cash we have is {self.cash}")
        # return super().after_market_closes()

    # def on_abrupt_closing runs when the strategy execution gets interrupted. 
    # Use this lifecycle method to execute code to stop trading gracefully like selling all assets
    def on_abrupt_closing(self):
        self.log_message("Abrupt closing")
        self.sell_all()
        # return super().on_abrupt_closing()

    # def on_bot_crash lifecycle method runs when the strategy crashes. By default, if not overloaded, it calls on_abrupt_closing
    def on_bot_crash(self, error):
        self.log_message(error)
        self.sell_all()
        # return super().on_bot_crash(error)

    # def on_new_order lifecycle method runs when a new order has been successfuly submitted to the broker
    def on_new_order(self, order):
        self.log_message(f"New order for SPY: {order}")
        # return super().on_new_order(order)

    # def on_partially_filled_order is called when an order has been partially filled by the broker
    def on_partially_filled_order(self, order, price: float, quantity: int, multiplier: float):
        missing = order.quantity - quantity
        self.log_message(f"Partially filled {quantity} order for SPY: {order}, price: {price}, missing: {missing}, multiplier: {multiplier}")

    # def on_filled_order is called when an order has been successfuly filled by the broker.
    def on_filled_order(self, position, order, price: float, quantity: float, multiplier: float):
        self.log_message(f"Filled {quantity} order for SPY: {order}, price: {price}, multiplier: {multiplier}")
        self.positions[order.asset] = position

    # def on_canceled_order is called when an order has been successfully canceled by the broker
    def on_canceled_order(self, order):
        self.log_message(f"{order} has been canceled by the broker")
        # return super().on_canceled_order(order)

    # def on_parameters_updated gets called when the strategy's parameters were updated using the self.update_parameters()
    def on_parameters_updated(self, parameters: dict):
        self.log_message(f"Parameters updated: {parameters}")
        # return super().on_parameters_updated(parameters)

# Instantiate the Trader, Alpaca, and Strategy Classes
trader = Trader(backtest=True)
broker = Alpaca(ALPACA_CONFIG)
strategy = MyStrategy(name="My Strategy",
                      budget=10000, 
                      broker=broker,
                      symbol="SPY")

# Create two trading fees, one that is a percentage and one that is a flat fee
trading_fee_1 = TradingFee(flat_fee=5)     # $5 flat fee
trading_fee_2 = TradingFee(percent_fee=.01) # 1% trading fee

# Backtest the Strategy (Optional)
backtesting_start = datetime(2024,4,1)
backtesting_end = datetime(2024,6,31)

# Start the profiler
yappi.start()

strategy.backtest(
    YahooDataBacktesting,
    backtesting_start,
    backtesting_end,
    parameters={
        "symbol": ["SPY", "AAPL"],
    },
    buy_trading_fees=[trading_fee_1, trading_fee_2],
    sell_trading_fees=[trading_fee_1, trading_fee_2],
)

# Stop the profiler
yappi.stop()

# Save the results
threads = yappi.get_thread_stats()
for thread in threads:
    print("Function stats for (%s) (%d)" % (thread.name, thread.id))

# Run the strategy
trader.add_strategy(strategy=strategy)
trader.run_all()


# Run the backtest
# trader = Trader(backtest=True)
# data_source = YahooDataBacktesting(
#     datetime_start=backtesting_start,
#     datetime_end=backtesting_end,
# )
# broker = BacktestingBroker(data_source)
# strat = MyStrategy(
#     broker=broker,
# )
# trader.add_strategy(strat)
# trader.run_all()