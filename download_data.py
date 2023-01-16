# import important libraries and functions
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf




# This function downloads the historical data for a list of stocks
def download_data(
        start_date,
        end_date,
        symbols,
    ):

    # Apply yf override function
    yf.pdr_override()

    # use pdr function to gert data from yahoo
    print(f"Getting DATA for {symbols}...")
    data = pdr.get_data_yahoo(symbols, start_date, end_date)['Close']
    data = pd.DataFrame(data)

    # move the date index into the dataframe as a column
    data = data.reset_index()

    # Convert Datetime formats
    data['Date'] = pd.to_datetime(data['Date'], utc=True)

    # make the date column the index
    data.index = data['Date']
    data = data[['Close']].copy()

    # Rename close column header
    new_name = f"{symbols}_Close"
    data.rename(columns={'Close':new_name}, inplace=True)
   
    # write to a .pkl file
    data.to_pickle(f"C:\Python Projects\SMA Indicator\DATA\{symbols} DATA.pkl")