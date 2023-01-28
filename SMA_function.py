# import important libraries and functions
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
# custom functions
from download_data import download_data


def calculate_sma(
        start_date,
        end_date,
        symbol,
    ):
        # get data for symbol
        data = download_data(start_date, end_date, symbol)
        
        if data.empty:
            pass
        
        else:
            # Calculate SMAs
            close = data['Close']
            sma50 = data['Close'].rolling(50).mean()
            sma100 = data['Close'].rolling(100).mean()
            sma200 = data['Close'].rolling(200).mean()
        
            # Create a column that tells us if RSI is > 50 or not
            data.loc[sma50 < close, '50_SMA_test'] = 'Y'
            data.loc[sma50 >= close, '50_SMA_test'] = 'N'
            data.loc[sma100 < close, '100_SMA_test'] = 'Y'
            data.loc[sma100 >= close, '100_SMA_test'] = 'N'
            data.loc[sma200 < close, '200_SMA_test'] = 'Y'
            data.loc[sma200 >= close, '200_SMA_test'] = 'N'

            return data

