
# pip install plotly
# https://analyticsindiamag.com/hands-on-guide-to-using-yfinance-api-in-python/

import plotly.graph_objects as go
import lib.yfinance_helper as yfh


#pfizer = yfh.getStock("PFE")

pfizer = yfh.getStockDataFromSymbol("PFE")


#pfizer.head()
#exit()

old= pfizer #<class 'pandas.core.frame.DataFrame'>
old = old.reset_index()

for i in ['Open', 'High', 'Close', 'Low']: 
      old[i]  =  old[i].astype('float64')


fig = go.Figure(data=[go.Candlestick(x=old['Date'],
                                   open=old['Open'],
high=old['High'],
low=old['Low'],
close=old['Close'])])

fig.show()