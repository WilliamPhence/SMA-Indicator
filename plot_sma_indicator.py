# Import Libraries and functions
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Declare Plot variables
def plot_sma_indy(df, etf, start_date, end_date, interval):
    # Declare figure and axes variables
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()

    line_name = f'{etf.upper()}_Close'

    line_etf, = ax1.plot(
            df[line_name], 
            label='SPY',
            )
    line_sma_y, = ax2.plot(
            df['Y'], 
            label='%'+f' of {etf} Components w/ over {interval} SMA',
            c='red'
            )

    # Plot lines & format figure
    # Format and create legend
    fig.legend(
        (
        line_etf, 
        line_sma_y, 
        ), 
        (
        f'{etf.upper()}',
        '%'+f' of {etf.upper()} Components w/ SMA over 50', 
        ),
        loc='upper right',
    )

    # Format the axes
    ax1.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b\n%Y'))
    ax1.set_title(f'{etf.upper()} vs {etf.upper()} Components SMA Distribution ({start_date}) to ({end_date})')
    ax1.set_ylabel(f"{etf.upper()}")
    ax2.set_ylabel('%'+f' of {etf.upper()} Comp. > {interval} SMA')
    ax1.set_xlabel('Dates (Month-Year)')

    print(df)

    # Save the figures and show the plots    
    plt.savefig(f"C:\Python Projects\SMA Indicator\\figures\{etf.upper()} {interval}-SMA Distributions {start_date} - {end_date}.png", dpi=1000, bbox_inches='tight', pad_inches=0.5)