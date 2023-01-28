# import important libraries and functions
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
from datetime import datetime
import datetime
from get_today import get_today


# This function downloads the historical data for a list of stocks
def download_data(
        start_date,
        end_date,
        symbol,
    ):
    try:
        # Apply yf override function
        yf.pdr_override()

        # use pdr function to gert data from yahoo
        print(f"Getting DATA for {symbol}...")
        data = pdr.get_data_yahoo(symbol, start_date, end_date)['Close']
        data = pd.DataFrame(data)

        # move the date index into the dataframe as a column
        data = data.reset_index()

        # Convert Datetime formats
        data['Date'] = pd.to_datetime(data['Date'], utc=True).dt.date

        # Get today's date and time to see if we need to get today's data
        now = datetime.datetime.now()
        weekday = now.weekday()
        hour = now.hour
        if weekday >= 1 and weekday <= 4:
            if hour >= 17:
                today = get_today(symbol)
                data = pd.concat([data, today], ignore_index=True)
                pass

        # return final dataframe
        return data

    except ValueError:
        print(f"Failed to download {symbol} DATA")