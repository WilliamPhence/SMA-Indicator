import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

#This is currently not in production
yf.pdr_override()

def get_today(symbol):

    stock = yf.Ticker(symbol)
    # Download the most recent trading data for the stock
    data = stock.history(period="1d")

    # Get the most recent closing price
    closing_price = data["Close"][-1]
    today = datetime.today().date()

    df = pd.DataFrame({
        'Date' : [today],
        'Close': [closing_price],
    })
    print(df)
    df.to_pickle('C:\Python Projects\SMA Indicator\DATA\\todays close DATA.pkl')

get_today("AAPL")