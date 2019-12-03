# https://www.youtube.com/playlist?list=PLQVvvaa0QuDcOdF96TBtRtuQksErCEBYZ
# %%
import os

import datetime as dt

import pandas as pd
import pandas_datareader as web

from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.dates  as mdates

from  mpl_finance import candlestick_ohlc

import requests
from bs4 import BeautifulSoup

import pickle

import numpy as np

style.use('ggplot')


# %%
# doesn't work for 2019 data
# tsla = web.DataReader('WIKI/TSLA',
#     'quandl', start='2018-01-01', end='2018-01-10',
#     api_key='')
# tsla.head()

# still seems to work
df = web.DataReader('AAPL',
                    'yahoo',
                    start=dt.datetime(2015, 1, 1),
                    end=dt.datetime.now())

df.to_csv('aapl.csv')

# %%

df.reset_index(inplace=True)
df.set_index('Date', inplace=True)
df.head()

# Adj Close is stock price adjusted to stock splits

# %%
df = pd.read_csv('data/tsla.csv', parse_dates=True, index_col=0)

# draw one columns. Index column is used for x-axis
# df[['Open', 'Adj Close']].plot()

# draw two columns
df[['Open', 'Adj Close']].plot()


#%%
# part 3
df = pd.read_csv('data/tsla.csv', parse_dates=True, index_col=0)

# add new column with 100 day average
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
df['50ma'] = df['Adj Close'].rolling(window=50, min_periods=0).mean()

df.columns

#%%

# plot everything
#df[['50ma', '100ma', 'Adj Close']].plot()

fig = plt.figure(figsize=(12,8))

ax1 = fig.add_subplot(311)
ax1.plot(df.index, df['Adj Close'])

ax2 = fig.add_subplot(312)
ax2.plot(df.index, df[['100ma', '50ma']])

ax3 = fig.add_subplot(313)
ax3.bar(df.index, df['Volume'])

# save as png in high resolution
# needs to happen before plt.show()
plt.savefig('data/rolling.png', dpi=400)

plt.show()

#%%
# part 4

# ohlc - open high low close
df = pd.read_csv('data/tsla.csv', parse_dates=True, index_col=0)
# resample data to 10 days
df_ohlc = df['Adj Close'].resample('10D').ohlc()

# total volume for 10 day periods
df_volume = df['Volume'].resample('10D').sum()

# remove index and rename to "Date" column. A new row_counter index is added
df_ohlc.reset_index(inplace=True)

# candlestick needs mdates instead of datetime
df_ohlc['Date'] = mdates.date2num(df_ohlc['Date'].values)


# need to reformat dates
date_format = mdates.DateFormatter('%d-%m-%Y')

# create chart
fig = plt.figure(figsize=(12,8))
ax1 = fig.add_subplot(211)
ax1.xaxis.set_major_formatter(date_format)
candlestick_ohlc(ax1, df_ohlc.values, width=4, colorup='#53c156', colordown='#ff1717')

ax2 = fig.add_subplot(212)
ax2.xaxis.set_major_formatter(date_format)
ax2.fill_between(mdates.date2num(df_volume.index.values), df_volume.values, 0)

# plt.savefig('data/candlestick.png', dpi=400)
plt.show()

#%%
# part 5
# SP500 is the top 500 most valuable companies
# value of company = number of outstanding shares * price

def save_sp500_tickers():
    website = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies').text
    soup = BeautifulSoup(website, 'lxml')
    table = soup.find('table',{'class':'wikitable sortable'})
    tickers = []
    for r in table.findAll('tr')[1:]:
        tickers.append(r.findAll('td')[0].text[:-1])
        
    with open('data/sp500_tickers.pickle', 'wb') as fp:
        pickle.dump(tickers, fp)

    print(tickers)



#%%
# part 6
def get_data_from_yahoo(reload_from_tickers_from_web=False):
    if reload_from_tickers_from_web:
        save_sp500_tickers()
    else:
        with open('data/sp500_tickers.pickle', 'rb') as fp:
            tickers = pickle.load(fp)
        print(f'found {len(tickers)} tickers')

        folder = 'sp500'

        if not os.path.exists(folder):
            os.makedirs(folder)
        
        start = dt.datetime(2000,1,1)
        end = dt.datetime.today()

        for ticker in tickers:
            
            filename = os.path.join(folder, ticker + '.csv')
            if not os.path.exists(filename):
                print(ticker)
                df = web.DataReader(ticker, 'yahoo', start=start, end=end)
                df.to_csv(filename)

get_data_from_yahoo()        


#%%
start = dt.datetime(2000,1,1)
end = dt.datetime.today()

df = web.DataReader('BRK-B', 'yahoo', start=start, end=end)
df.to_csv('BRKB.csv')

#%%
# part 7
def compile_data():
    with open('data/sp500_tickers.pickle', 'rb') as fp:
        tickers = pickle.load(fp)
    
    folder = 'sp500'

    main_df = pd.DataFrame()

    for count, ticker in enumerate(tickers):
        print(count, ticker)
        filename = os.path.join(folder, ticker + '.csv')
        df = pd.read_csv(filename)
        df.set_index('Date', inplace=True)
        df.rename(columns={'Adj Close': ticker}, inplace=True)
        df = df.filter(['Date', ticker])
       
        if main_df.empty:
            main_df = df
        else:
            # make an outer join to insert all rows. If a row doesn't already exists
            # a new row 
            main_df = main_df.join(df, how='outer')

    main_df.to_csv('sp500_join_closes.csv')


compile_data()

#%%
# part 8    

def load_data():
    df = pd.read_csv('sp500_join_closes.csv', index_col=0)
    # df[['AAPL', 'MMM']].plot()
    return df.corr()

df = load_data()

#%%
# creat a heatmap of all companies correlations
def visualize_data(df):
    # if correlation between two companies is 0 then there is not much
    # correlation and the two companies could be used to diversify our
    # portfolio

    # in case both stock have negative correlation one stock could hold
    # and the other be shorted
    
    # get all values (no index and no headers) from data frame
    values = df.values
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    
    # Red to Yellow (neutral) to Green
    heatmap = ax.pcolor(values, cmap=plt.cm.RdYlGn)
    fig.colorbar(heatmap)
    
    # move the ticks to the middle of a cell
    ax.set_xticks(np.arange(values.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(values.shape[1]) + 0.5, minor=False)
    
    # remove gap
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    columns_labels = df.columns
    row_labels = df.columns

    ax.set_xticklabels(columns_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    
    # set color limits
    heatmap.set_clim(-1,1)

    plt.tight_layout()
    # plt.savefig('sp500_corr_heatmap.png', dpi=600)
    
    # plt.show()



visualize_data(df)


# %%
# part 9
# pricing data to percentage changed to normalize data
# percentage changed data are the feature
# buy, sell, hold will be the labels

# prices goes up 2% -> buy
# prices goes down 2% -> sell
# else -> hold

def process_data_for_labels(ticker, df):
    hm_days = 7

    # all tickers
    tickers = df.columns.values
    df.fillna(0, inplace=True)
    
    for i in range(1, hm_days+1):
        df[f'{ticker}_{i}d'] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df

process_data_for_labels('TSLA', df)


