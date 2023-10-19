import os
import requests
import time
import pandas as pd
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from MCForecastTools import MCSimulation

load_dotenv()

#Part 1 - Personal Finance Planner
#Collect Crypto Prices Using the `requests` Library

crypto_assets = float(os.getenv("CRYPTO_ASSETS"))
print(f"Current Crypto Assets: {crypto_assets}")

# Crypto API URLs
btc_url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=CAD"
eth_url = "https://api.alternative.me/v2/ticker/Ethereum/?convert=CAD"

# Crypto API URLs
btc_url = "https://api.alternative.me/v2/ticker/Bitcoin/?convert=CAD"
eth_url = "https://api.alternative.me/v2/ticker/Ethereum/?convert=CAD"

headers = {
      'Content-Type': 'application/json',
      'accept': 'application/json',
}

# Fetch current BTC price
btc_response = requests.get(btc_url, headers=headers)
btc_data = btc_response.json()
btc_price_cad = btc_data["data"]["1"]["quotes"]["CAD"]["price"]

# Fetch current ETH price
eth_response = requests.get(eth_url, headers=headers)
eth_data = eth_response.json()
eth_price_cad = eth_data["data"]["1027"]["quotes"]["CAD"]["price"]

# Define the amount of BTC and ETH you own 
crypto_assets = {
    "BTC": 1.2,
    "ETH": 5.3
}

# Compute current value of your crypto assets
total_value_cad = (crypto_assets["BTC"] * btc_price_cad) + (crypto_assets["ETH"] * eth_price_cad)

# Print the results
print(f"Current BTC Price (CAD): {btc_price_cad}")
print(f"Current ETH Price (CAD): {eth_price_cad}")
print(f"Your Crypto Assets:")
for crypto, amount in crypto_assets.items():
    print(f"{crypto}: {amount}")
print(f"Total Value (CAD): {total_value_cad}")

# Collect Investments Data Using Alpaca: SPY (stocks) and AGG (bonds)
# Set current amount of shares
my_agg = 200
my_spy = 50

# Set Alpaca API key and secret
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_api_secret = os.getenv("ALPACA_API_SECRET")
# Create the Alpaca API object
api = tradeapi.REST(
    alpaca_api_key, 
    alpaca_api_secret, 
    api_version="v2"
    )

account = api.get_account()
print(f"Account ID: {account.id}")
print(f"Account Status: {account.status}")
print(f"Buying Power: ${account.buying_power}")
