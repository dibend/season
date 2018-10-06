# seasonality
Try to find some seasonality in stock prices from yahoo finance historical csv data.

This program looks at each pair of trading days every year and determines which would've had the best performance in attempt to find seasonal patterns.

Download historical data from Yahoo Finance and delete top line of column names and any lines containing null values.

e.g. link https://finance.yahoo.com/quote/AAPL/history?period1=347173200&period2=1538798400&interval=1d&filter=history&frequency=1d

Make sure the start date is the first trading day of a year.

run python season.py AAPL.csv

replacing AAPL.csv with whichever stock you chose 

The last 2 lines printed will be the best trading days to buy and sell, followed by the ratio of the return.
