
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


# WARNING! The `decimal_to_precision` method is susceptible to getcontext().prec!
def decimal_to_precision(n, rounding_mode=ROUND, precision=None, counting_mode=DECIMAL_PLACES, padding_mode=NO_PADDING):
