# import important libraries and functions
import pandas as pd
from SMA_function import calculate_sma
from download_data import download_data
from get_symbols import get_symbol_list


# Grab data and run RSI test 
def get_sma_dist(        
        start_date,
        end_date,
        etf,
    ):
    # Grab user selected ETF data
    download_data(        
        start_date,
        end_date,
        etf,
    )

    # put data into main_df
    main_df = pd.read_pickle(f"C:\Python Projects\SMA Indicator\DATA\{etf} DATA.pkl")
    main_df = pd.DataFrame(main_df)

    # Change Indexing from dates to integers
    main_df = main_df.reset_index(names="Date")
    
    # Convert Datetime format
    main_df['Date'] = pd.to_datetime(main_df['Date'], utc=True).dt.date

    # create an empty list to store symbols with failed downloads
    failed_downloads = []

    # Get the list of symbols for the components of the ETF chosen
    get_symbol_list(etf)
    
    symbols = pd.read_pickle("C:\Python Projects\SMA Indicator\DATA\symbol list.pkl")

    # Run RSI function for each symbol
    for symbol in symbols:

        # Download data for all symbols and see if RSI is over 50 or not
        # This function also creates a csv file for each symbol that is used in the try block below
        calculate_sma(
                start_date,
                end_date, 
                symbol
        )

        # Add each Symbol's RSI_test results to a main data frame that contains SPY & Date Data
        try: 
            # try using the data frame
            data = pd.read_pickle(f"C:\Python Projects\SMA Indicator\DATA\{symbol} DATA.pkl")            
            # pass each new pkl file into a temporary data frame
            data = pd.DataFrame(data)

            # Reduce data frame to only needed columns
            data = data[['Date','RSI_test']].copy()

            # Convert Datetime format
            data['Date'] = pd.to_datetime(data['Date'], utc=True).dt.date

            # Rename Column headers
            new_name = f"{symbol}_rsi_test"
            data.rename(columns= {'RSI_test':new_name}, inplace = True)
            
            # add the RSI test column to the main_df
            main_df = pd.merge(main_df, data, how='outer', on=['Date'])

        # Add an exception for when there are symbols on the list without available data
        except FileNotFoundError:
            failed_downloads.append(symbol)
            print(f"No data for {symbol}")

    # Select only the columns starting from the third column
    # Get the distribution of values in each row
    dist_df = main_df.iloc[:, 2:].apply(lambda x: x.value_counts(normalize=True), axis=1)

    # add the RSI test column to the main_df
    main_df = pd.concat([main_df, dist_df], axis=1)

    # Remove RSI_test columns
    close_col = f'{etf}_Close'
    main_df = main_df[['Date', close_col, 'Y', 'N']].copy()

    # print a list of failed downloads
    if failed_downloads:
        print("\nList of failed downloads:")
        for name in failed_downloads:
            print(name)
    else:
        print("No Failed Downloads\n")

    # print main_df to pkl
    main_df.to_pickle(f"C:\Python Projects\SMA Indicator\DATA\ 000_FINAL_DATA.pkl")