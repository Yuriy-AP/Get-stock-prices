# Get-stock-prices

There are several ways to go around getting daily stock prices for free. For example, these are some of the possibilities.
1) Yahoo Finance
2) Alpha Vantage
3) Quandl (free access is limited to the data significantly lagged in time)

The provided code performs the following: 
1) Scrap S&P500 constituents from Wikipedia
2) Obtain closing daily stock prices from Quandl, using pandas_datareader.
One needs to modify some details, for example, the path to the folder to store the results. 
