
import ccxt
import logging

# Switch to Sandbox using exchange.setSandboxMode(true) or 
# exchange.set_sandbox_mode(true) immediately after creating the exchange 
# before any other call!
exchange = ccxt.binance(config)
exchange.set_sandbox_mode(True)    # This has to be the first call immediately after creating the exchange (before any other calls)

# Pythonic way of DEBUG logging with a pythonic logger
logging.basicConfig(level=logging.DEBUG)