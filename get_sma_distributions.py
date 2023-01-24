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
    main_df = download_data(        
        start_date,
        end_date,
        etf,
    )

    # put data into main_df
    main_df = pd.DataFrame(main_df)
    # Change Indexing from dates to integers
    main_df = main_df.reset_index(names="Date")    
    # Convert Datetime format
    main_df['Date'] = pd.to_datetime(main_df['Date'], utc=True).dt.date
    # Make 3 identical copies of main_df
    main50_df = main_df
    main100_df = main_df
    main200_df = main_df

    # create an empty list to store symbols with failed downloads
    failed_downloads = []
    
    # Get the list of symbols for the components of the ETF chosen    
    symbols = get_symbol_list(etf)

    # Run RSI function for each symbol
    for symbol in symbols:

        # Download data for all symbols and see if RSI is over 50 or not
        # This function also creates a csv file for each symbol that is used in the try block below
        data = calculate_sma(
                start_date,
                end_date, 
                symbol
        )

        # Add each Symbol's RSI_test results to a main data frame that contains SPY & Date Data
        try:    
            # pass each new pkl file into a temporary data frame
            data = pd.DataFrame(data)

            # Reduce data frame to only needed columns
            data50 = data[['Date', '50_SMA_test']].copy()
            data100 = data[['Date', '100_SMA_test']].copy()
            data200 = data[['Date', '200_SMA_test']].copy()

            # Convert Datetime format
            data50['Date'] = pd.to_datetime(data50['Date'], utc=True).dt.date
            data100['Date'] = pd.to_datetime(data100['Date'], utc=True).dt.date
            data200['Date'] = pd.to_datetime(data200['Date'], utc=True).dt.date

            # Rename Column headers
            new_name = f"{symbol}50sma_test"
            data50.rename(columns= {'50_SMA_test':new_name}, inplace = True)
            new_name = f"{symbol}100sma_test"
            data100.rename(columns= {'100_SMA_test':new_name}, inplace = True)
            new_name = f"{symbol}200sma_test"
            data200.rename(columns= {'200_SMA_test':new_name}, inplace = True)
            
            # add the test column to the main_df
            main50_df = pd.merge(main50_df, data50, how='outer', on=['Date'])
            main100_df = pd.merge(main100_df, data100, how='outer', on=['Date'])
            main200_df = pd.merge(main200_df, data200, how='outer', on=['Date'])

        # Add an exception for when there are symbols on the list without available data
        except KeyError:
            failed_downloads.append(symbol)
            print(f"No data for {symbol}")
    
    
    # Select only the columns starting from the third column
    # Get the distribution of values in each row
    dist50_df = main50_df.iloc[:, 2:].apply(lambda x: x.value_counts(normalize=True), axis=1)
    dist100_df = main100_df.iloc[:, 2:].apply(lambda x: x.value_counts(normalize=True), axis=1)
    dist200_df = main200_df.iloc[:, 2:].apply(lambda x: x.value_counts(normalize=True), axis=1)

    # add the RSI test column to the main_df
    main50_df = pd.concat([main50_df, dist50_df], axis=1)
    main100_df = pd.concat([main100_df, dist100_df], axis=1)
    main200_df = pd.concat([main200_df, dist200_df], axis=1)

    # Remove test columns
    close_col = f'{etf}_Close'
    main50_df = main50_df[['Date', close_col, 'Y', 'N']].copy()
    main100_df = main100_df[['Date', close_col, 'Y', 'N']].copy()
    main200_df = main200_df[['Date', close_col, 'Y', 'N']].copy()

    # print a list of failed downloads
    if failed_downloads:
        print("\nList of failed downloads:")
        for name in failed_downloads:
            print(name)
    else:
        print("No Failed Downloads\n")

    # print main_dfs to pkl
    main50_df.to_pickle("C:\Python Projects\SMA Indicator\DATA\ 050_FINAL_DATA.pkl")
    main100_df.to_pickle("C:\Python Projects\SMA Indicator\DATA\ 100_FINAL_DATA.pkl")
    main200_df.to_pickle("C:\Python Projects\SMA Indicator\DATA\ 200_FINAL_DATA.pkl")