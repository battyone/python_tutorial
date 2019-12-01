# %%
import datetime as dt
import pandas as pd
import pandas_datareader as web
import os

# %%
# doesn't work for 2019 data
# tsla = web.DataReader('WIKI/TSLA',
#     'quandl', start='2018-01-01', end='2018-01-10',
#     api_key='')
# tsla.head()

# still seems to work
df = web.DataReader('TSLA',
                    'yahoo',
                    start=dt.datetime(2015, 1, 1),
                    end=dt.datetime.now())
# %%

df.reset_index(inplace=True)
df.set_index('Date', inplace=True)
df.head()

# Adj Close is stock price adjusted to stock splits

# %%
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

df.head()
