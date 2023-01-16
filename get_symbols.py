import pandas as pd
import requests as req
import csv


def get_symbol_list(etf):
    if etf == 'SPY':
        # Get the list of symbols for the components of the ETF chosen
        symbols = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]['Symbol'].tolist()
    
    elif etf == 'QQQ':
        # Send a request to the URL
        response = req.get('https://www.invesco.com/us/financial-products/etfs/holdings/main/holdings/0?audienceType=Investor&action=download&ticker=QQQ')

        # Parse the CSV data
        reader = csv.reader(response.text.splitlines())

        # Write the data to a new CSV file
        with open('C:\Python Projects\SMA Indicator\DATA\qqq_holdings.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for row in reader:
                writer.writerow(row)

        symbols = pd.read_csv("C:\Python Projects\SMA Indicator\DATA\qqq_holdings.csv")
        symbols = pd.DataFrame(symbols)

        symbols = symbols['Holding Ticker'].copy()
    
    elif etf == 'IWM':
        # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\russell_2000.xlsx"

        # Read the data file into a pandas dataframe
        symbols = pd.read_excel(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\russell_2000.pkl")
    
    elif etf == "XLE":

        # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xle.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xle.pkl")
    
    elif etf == "XLY":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xly.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xly.pkl")
    
    elif etf == "XLP":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlp.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlp.pkl")
    
    elif etf == "XLV":
        # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlv.CSV"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlv.pkl") 
    
    elif etf == "XLB":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlb.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlb.pkl")
    
    elif etf == "XLRE":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlre.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlre.pkl")  
    
    elif etf == "XLK":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlk.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlk.pkl")  
    
    elif etf == "XLU":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlu.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlu.pkl")   
    
    elif etf == "XLC":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlc.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xlc.pkl")

    elif etf == "XLI":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xli.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xli.pkl")

    elif etf == "XLF":
                # Declare datafile location
        file = "C:\Python Projects\SMA Indicator\STATIC DATA\\xlf.csv"

        # Read the data file into a pandas dataframe
        symbols = pd.read_csv(file)
        symbols = pd.DataFrame(symbols)
        # Copy the list of tickers
        symbols = symbols['Ticker'].copy()

        # Save list to a pkl file
        symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\\xli.pkl")  
    
    else:
        print("Not an acceptable input, try again")
       
  
    # sort list alphabetically
    symbols = sorted(symbols)
    # convert list to pandas series
    symbols = pd.Series(symbols)
    # save series to pkl file
    symbols.to_pickle("C:\Python Projects\SMA Indicator\DATA\symbol list.pkl")