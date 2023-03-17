#pip install yfinance

import yfinance as yf

data = yf.download("SPY", start="2021-01-01", end="2021-12-31")

print(data)

data.to_excel("spy.xlsx")
