"""
Created on Sat Feb 10 11:04:34 2018
@author: Yuriy
"""

import os
import pandas as pd
from datetime import datetime
import requests
from bs4 import BeautifulSoup

os.chdir(' ... Your File Path Here ...')

# (1) Input needed dates:
start = datetime(2011, 1, 1)
end = datetime(2018, 2, 1)

# (2) Scrap S&P500 stocks:
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

webpage = requests.get(url)
webpage.raise_for_status
soup = BeautifulSoup(webpage.text, "lxml")
tables = soup.find_all('table')

tables[0]
tables_data = tables[0].select('tr')

N = len(tables_data) - 1
Columns = ['Ticker', 'Name', 'Industry', 'Subindustry']
SPSTOCKS = pd.DataFrame(columns=Columns)


#Tickers:
tables_data[1].select('td')[0].getText()
tables_data[1].select('td')[1].getText()
tables_data[1].select('td')[3].getText()
tables_data[1].select('td')[4].getText()

for i in range(N):
    ticker = tables_data[i+1].select('td')[0].getText()
    name = tables_data[i+1].select('td')[1].getText()
    industry = tables_data[i+1].select('td')[3].getText()
    subind = tables_data[i+1].select('td')[4].getText()
    SPSTOCKS = SPSTOCKS.append(pd.DataFrame([[ticker, name, industry, subind]], 
                                            columns=Columns))
SPSTOCKS.iloc[0:3,:]
len(SPSTOCKS)
SPSTOCKS.to_csv('S&P500.csv',encoding='utf-8')



# (3) Get daily prices - closign adjusted:
import pandas_datareader.data as web

STOCKS = pd.read_csv('S&P500.csv')
Tickers = STOCKS['Ticker']
Tickers.head(5)
Tickers.values

ALLPRICES = pd.DataFrame(columns=Tickers)
Tickers_small = Tickers[0:5]
for stock in Tickers:
    name = stock+'.US'
    try:
        f = web.DataReader(name, 'quandl', start, end)
        ALLPRICES[stock] = f['AdjClose']
        print(stock, "\n")
    except:
        print(stock, " was not obtained!")
        continue
# http://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-quandl
f1 = web.DataReader('MMM.US', 'quandl', start, end)
f1.head(5)

"""
for UK stocks:
f2 = web.DataReader('TSCO.UK', 'quandl', start, end)
f2.head(5)
"""
L1=len(ALLPRICES.columns)
ALLPRICES.head(5)
len(ALLPRICES)

ALLPRICES1=ALLPRICES.dropna(axis=1,how='all')
L2=len(ALLPRICES1.columns)
print(L1," ",L2)

ALLPRICES1.to_csv('S&P500_Prices.csv',encoding='utf-8')

 
