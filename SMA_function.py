# import important libraries and functions
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime
# custom functions
from get_today import get_today


def calculate_sma(
        start_date,
        end_date,
        symbol
    ):

    try:
        # Apply yf override function
        yf.pdr_override()

        # Obtain data, show terminal output for each download attempt
        print(f"Getting Yahoo Data for {symbol}....")
        data = pdr.get_data_yahoo(symbol, start_date, end_date)['Close']
        # Take the data we just downloaded and put it into a pandas dataframe
        data = pd.DataFrame(data)

        # Change Indexing from dates to integers
        data = data.reset_index(names="Date")

        # Get today's date and time to see if we need to get today's data
        now = datetime.datetime.now()
        weekday = now.weekday()
        hour = now.hour
        if weekday >= 1 and weekday <= 4:
            if hour >= 17:
                today = get_today(symbol)
                data = pd.concat([data, today], ignore_index=True)
                pass

        # Convert Datetime formats
        data['Date'] = pd.to_datetime(data['Date'], utc=True)

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


    except ValueError:
        print(f"Failed to download {symbol} DATA")
        print(data)

