import lib.yfinance_helper as yfh


stock_data = yfh.getStockDataFromSymbol("MSFT")
print(type(stock_data))#<class 'pandas.core.frame.DataFrame'>
print(stock_data)







