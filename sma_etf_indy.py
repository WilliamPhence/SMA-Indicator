# Import Libraries and functions
from get_sma_distributions import get_sma_dist
from plot_sma_indicator import plot_sma_indy
from delete_temp_files import delete_temp_files
from datetime import date
import pandas as pd



def sma_etf_indy():

    # Declare path for the temp data to be deleted after plots are shown and saved
    temp_data = 'C:\Python Projects\SMA Indicator\DATA'

    # ask use to select from a menu of ETFs
    print("You can select from one of the following ETF's to plot the SMA Distribution indicator for:")
    print("\tSPY - S&P500")
    print("\tQQQ - NASDAQ 100")
    print("\tIWM - RUSSELL 2000")
    print("\tXLY - CONSUMER DISCRETIONARY")
    print("\tXLP - CONSUMER STAPLES")
    print("\tXLY - FINANCIALS")
    print("\tXLV - INDUSTRIALS")
    print("\tXLB - MATERIALS")
    print("\tXLRE - REAL ESTATE")
    print("\tXLK - TECHNOLOGY")
    print("\tXLU - UTILITIES")
    print("\tXLC - COMMUNICATION SERVICES")

    # Get user inputs
    etf = input("\nENTER ONE OF THE TICKERS : ")
    start_date = input("Enter the start date (YYYY-MM-DD) : ")
    end_date = input("Enter the end date (YYYY-MM-DD) or 'today' : ")

    # convert end_date to correct format if user enters 'today'
    if end_date.upper() == 'TODAY':
        end_date = date.today()
    else:
        end_date = end_date


    # call get_rsi_dist function and pass through user inputs
    get_sma_dist(
            start_date,
            end_date,
            etf.upper(),
    )

    # Declare datasource
    df = pd.read_pickle(f"C:\Python Projects\SMA Indicator\DATA\ 000_FINAL_DATA.pkl") 
    # Set datasource as a dataframe and set date column as the index
    df = pd.DataFrame(df)
    df.set_index('Date', inplace=True)

    plot_sma_indy(df, etf, start_date, end_date)
    
    delete_temp_files(temp_data)


while True:
    sma_etf_indy()
    repeat = input("Are you done? Y/N : ")
    if repeat.upper() == "N":
        continue
    elif repeat.upper() == 'Y':
        break
