
from datetime import date

# Returns option chain for a particular exchange.
# Takes in a full set of chains for all the exchanges and returns on chain for 
# a given exchange. The full chains are returned from get_chains method.
asset = "SPY"
chain = self.get_chain(asset)
# Returns option chains.
# Obtains option chain information for the asset (stock) from each of the exchanges 
# the options trade on and returns a dictionary for each exchange.
asset = "SPY"
chains = self.get_chains(asset)


# Will return the greeks for SPY
# Will return all the greeks available. API Querying for prices and rates are expensive, 
# so they should be passed in as arguments most of the time.
opt_asset = Asset("SPY", expiration=date(2021, 1, 1), strike=100, option_type="call")
greeks = self.get_greeks(opt_asset)
implied_volatility = greeks["implied_volatility"]
delta = greeks["delta"]
gamma = greeks["gamma"]
vega = greeks["vega"]
theta = greeks["theta"]


# Will return the strikes for SPY
# Using the chains dictionary obtained from get_chains finds all the multiplier for the 
# option chains on a given exchange.
asset = "SPY"
strikes = self.get_strikes(asset)

# Will return the expiry dates for SPY
# Using the chains dictionary obtained from get_chains finds all expiry dates for the 
# option chains on a given exchange. The return list is sorted
asset = "SPY"
expiry_dates = self.get_expiration(asset)

# Will return the multiplier for SPY
# Using the chains dictionary obtained from get_chains finds all the multipliers 
# for the option chains on a given exchange.
asset = "SPY"
multiplier = self.get_multiplier(asset)

# Will return the date for the expiry
# Converts an IB Options expiry to datetime.date.
date1 = "20200101"
expiry_date = self.options_expiry_to_datetime_date(date1)
self.log_message(f"Expiry date for {date1} is {expiry_date}")

# Finds the next trading day for the given date and exchange.
# date: str, exchange: str
self.get_next_trading_day(self, date, exchange='NYSE')