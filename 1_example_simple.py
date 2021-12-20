
# pip install yfinance
# vgl. https://finance.yahoo.com/
import yfinance as yf
msft = yf.Ticker("MSFT")
print(msft.info)

