import yfinance as yf
import pandas as pd
import datetime

eft_assets = ["XAIX.MI", "DBXK.DE", "IQQH.DE", "PJAT.F", "D2WA.MU", "0P00001BIC.F", "0P00000PM7.F"]
comm_assets = ["GC=F"]
crypto_assets = ["URUS-USD", "AU-USD"]

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
