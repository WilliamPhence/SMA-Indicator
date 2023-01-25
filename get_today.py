import yfinance as yf
import pandas as pd
from datetime import date

# this function gets the closing price of today
def get_today(ticker):

    try:
        ticker_yahoo = yf.Ticker(ticker)
        data = ticker_yahoo.history()

        last_quote = data['Close'].iloc[-1]
        today = date.today()

        df = pd.DataFrame({'Date':[today], 'Close':[last_quote]})
        return df
    except IndexError:
        print(f"Failed to download today's {ticker} DATA")