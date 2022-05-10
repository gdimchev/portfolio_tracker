import yfinance as yf
import pandas as pd
import datetime
from misc.read_json import read_yaml

config = read_yaml(file=r'/Users/dimchev/PycharmProjects/portfolio_tracker/config/config.yml')
eft_assets = config['assets']['eft_assets']
comm_assets = config['assets']['comm_assets']
crypto_assets = config['assets']['crypto_assets']

assets = {"eft": eft_assets, "gold": comm_assets, "crypto": crypto_assets}

rows = []
for asset_type in assets:
    for asset in assets[asset_type]:
        msft = yf.Ticker(asset)
        row = {"Asset_type": asset_type,
               "Asset": asset,
               "Name": msft.info['shortName'],
               "Price": msft.info['regularMarketPrice'],
               "Currency": msft.info['currency'],
               "Date": datetime.datetime.now().strftime("%d/%m/%Y")}
        print(row)
        rows.append(row)

df = pd.DataFrame(rows)
