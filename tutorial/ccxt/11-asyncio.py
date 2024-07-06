
import asyncio
import ccxt.async_support as ccxt

# In async mode you have all the same properties and methods, but most methods are decorated 
# with an async keyword. If you want to use async mode, you should link against the 
# ccxt.async_support subpackage
async def print_poloniex_dogebtc_ticker():
    poloniex = ccxt.poloniex()
    print(poloniex.fetch_ticker('DOGE/BTC'))
    await poloniex.close()    # close the exchange if you no longer need it

asyncio.run(print_poloniex_dogebtc_ticker())