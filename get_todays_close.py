import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
from datetime import datetime

#This is currently not in production
yf.pdr_override()

def get_today(symbol):    

    # Get the most recent daily close price
    #closing_price = stock.info['regularMarketPreviousClose']
    closing_price = pdr.get_data_yahoo(symbol)["Close"]
    print(closing_price)
    closing_price = int(closing_price)
    print(closing_price)
    today = datetime.today().date()

    df = pd.DataFrame({
        'Date' : [today],
        'Close': [closing_price],
    })
    print(df)
    df.to_pickle('C:\Python Projects\SMA Indicator\DATA\\todays close DATA.pkl')

get_today("AAPL")