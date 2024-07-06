
from lumibot.traders import Trader
# Import interactive brokers
from lumibot.brokers import InteractiveBrokers
from lumibot.strategies.strategy import Strangle
from credentials import INTERACTIVE_BROKERS_CONFIG


INTERACTIVE_BROKERS_CONFIG = {
    "SOCKET_PORT": 7497,
    "CLIENT_ID": "your Master API Client ID three digit number",
    "IP": "127.0.0.1",
}

trader = Trader()
# Initialize interactive brokers
interactive_brokers = InteractiveBrokers(INTERACTIVE_BROKERS_CONFIG)

strategy = Strangle(broker=interactive_brokers)
trader.add_strategy(strategy)
trader.run_all()