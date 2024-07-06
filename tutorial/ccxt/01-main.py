
import ccxt

# print (ccxt.exchanges)

# Instantiate an Exchange
exchange = ccxt.okcoin()  # this is the default id
okcoin1 = ccxt.okcoin({'id': 'okcoin1'})
okcoin2 = ccxt.okcoin({'id': 'okcoin2'})
id = 'btcchina'
btcchina = eval('ccxt.%s ()' % id)
coinbasepro = getattr(ccxt, 'coinbasepro')
# From variable id
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
exchange = exchange_class({
    'apiKey': 'API_KEY',
    'secret': 'SECRET_KEY'
})

# Overriding Exchange Properties Upon Instantiation
exchange = ccxt.binance({
    'rateLimit': 10000,    # unified exchange property
    'headers': {
        'YOUR_CUSTOM_HTTP_HEADER': 'YOUR_CUSTOM_VALUE',
    },
    'options': {
        'adjustForTimeDifference': True,   # exchange-specific option
    }
})
exchange.options['adjustForTimeDifference'] = False

# Overriding Exchange Methods
ex = ccxt.binance()
def my_overload(symbol, params = {}):
    pass

ex.fetch_ticker(my_overload)
print(ex.fetch_ticker('BTC/USDT'))
