import pandas as pd
import matplotlib.pyplot as plt

from pandas_datareader import data
from datetime import datetime

# SETUP
tickers = ['BTC-USD', 'BRL=X']

def fetch_data(ticker):
    start = datetime(2020, 5, 1)
    end = datetime(2020, 6, 29)
    source = 'yahoo'
    return data.DataReader(ticker, source, start, end)

btc = fetch_data(tickers[0])
brl = fetch_data(tickers[1])

returns_brl = brl['Close'].pct_change().dropna()
returns_btc = btc['Close'].pct_change().dropna()

import seaborn as sns

def plot_returns():
    fig, (ax1, ax2) = plt.subplots(
        nrows=2,
        ncols= 1,
        sharex=True,
        sharey=True,
        figsize=(10, 6)
    )

    plt.xticks(rotation=45)
    fig.suptitle('BTC vs BRL price variation')

    ax1.set_title('BRL')
    ax1.plot(
        returns_brl.index,
        returns_brl.values,
        c='green'
    )

    ax2.set_title('BTC')
    ax2.plot(
        returns_btc.index,
        returns_btc.values,
        c='orange'
    )

plot_returns()
