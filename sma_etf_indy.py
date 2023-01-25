# Import Libraries and functions
from get_sma_distributions import get_sma_dist
from plot_sma_indicator import plot_sma_indy
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
    end_date = input("Enter the end date (YYYY-MM-DD) or 't' for today : ")

    # convert end_date to correct format if user enters 'today'
    if end_date.upper() == 'T':
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
    df50 = pd.read_pickle("C:\Python Projects\SMA Indicator\DATA\ 050_FINAL_DATA.pkl")
    df100 = pd.read_pickle("C:\Python Projects\SMA Indicator\DATA\ 100_FINAL_DATA.pkl")
    df200 = pd.read_pickle("C:\Python Projects\SMA Indicator\DATA\ 200_FINAL_DATA.pkl")
    # Set datasource as a dataframe and set date column as the index
    df50 = pd.DataFrame(df50)
    df100 = pd.DataFrame(df100)
    df200 = pd.DataFrame(df200)

    df50.dropna(inplace=True)
    df100.dropna(inplace=True)
    df200.dropna(inplace=True)

    df50.set_index('Date', inplace=True)
    df100.set_index('Date', inplace=True)
    df200.set_index('Date', inplace=True)

    plot_sma_indy(df50, etf, interval=50)
    plot_sma_indy(df100, etf, interval=100)
    plot_sma_indy(df200, etf, interval=200)


while True:
    sma_etf_indy()
    repeat = input("Press 'Enter' to go again\nEnter anything else to exit : ")
    if repeat.upper() == "":
        continue
    else:
        break