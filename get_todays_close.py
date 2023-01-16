import yfinance as yf
import pandas as pd
from datetime import datetime

#This is currently not in production

def get_today(symbol):

    yf.pdr_override()

    # Get the stock information
    stock = yf.Ticker(symbol)

    # Get the most recent daily close price
    most_recent_close = stock.info['regularMarketPrice']
    most_recent_close = int(most_recent_close)
    today = datetime.today().date()

    df = pd.DataFrame({
        'Date' : [today],
        'Close': [most_recent_close],
    })
    df.to_pickle('C:\Python Projects\SMA Indicator\DATA\\todays close DATA.pkl')