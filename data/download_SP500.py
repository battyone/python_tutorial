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

style.use('ggplot')

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
                if not '.' in ticker:
                    print(ticker)
                    df = web.DataReader(ticker, 'yahoo', start=start, end=end)
                    df.to_csv(filename)
                else:
                    a = ticker.replace('.', '-')
                    print(a)
                    df = web.DataReader(a, 'yahoo', start=start, end=end)
                    df.to_csv(filename)

get_data_from_yahoo()
