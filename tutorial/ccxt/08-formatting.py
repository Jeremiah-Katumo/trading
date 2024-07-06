
from ccxt.base.decimal_to_precision import DECIMAL_PLACES  # noqa E402
from ccxt.base.decimal_to_precision import TICK_SIZE  # noqa E402
from ccxt.base.decimal_to_precision import NO_PADDING  # noqa E402
from ccxt.base.decimal_to_precision import TRUNCATE  # noqa E402
from ccxt.base.decimal_to_precision import ROUND  # noqa E402
from ccxt.base.decimal_to_precision import SIGNIFICANT_DIGITS  # noqa E402
from ccxt.base.decimal_to_precision import PAD_WITH_ZERO  # noqa E402
from ccxt.base.decimal_to_precision import decimal_to_precision  # noqa E402
from ccxt.base.decimal_to_precision import number_to_string  # noqa E402
import ccxt  # noqa: F402
from ccxt.base.precise import Precise  # noqa E402


# enable built-in rate limiting upon instantiation of the exchange
exchange = ccxt.bitfinex({
    # 'enableRateLimit': True,  # enabled by default
})

# or watch the built-in rate-limiter on or off later after instantiation
exchange.enableRateLimit = True   # enable
exchange.enableRateLimit = False  # disable
# In case your calls hit a rate limit or get nonce errors, the ccxt library will throw an 'InvalidNonce' exception, 
# or, in some cases, one of the following types: 
# DDosProtection, ExchangeNotAvailable, ExchangeError, InvalidNonce


# WARNING! The `decimal_to_precision` method is susceptible to getcontext().prec!
def decimal_to_precision(n, rounding_mode=ROUND, precision=None, counting_mode=DECIMAL_PLACES, padding_mode=NO_PADDING):
    pass

def amount_to_precision (symbol, amount):
    pass

def price_to_precision (symbol, price):
    pass
def cost_to_precision (symbol, cost):
    pass

def currency_to_precision (code, amount):
    pass

# Load all available markets from the exchange before calling the above methods
exchange.load_markets()
symbol='BTC/USDT'
amount=1.2345678    # amount in base currency BTC
price=87654.321     # price in quote currency USDT
formatted_amount = exchange.amount_to_precision(symbol=symbol, amount=amount)
formatted_price = exchange.price_to_precision(symbol=symbol, price=price)
