


from collections.abc import Iterable
import yfinance

def getStockDataFromSymbol(symbol: str,period = '1y',interval= '1d'):
    
    stock = getStock(symbol)
    return stock.history(period, interval)



def getStock(symbol : str) -> yfinance.Ticker:
    if symbol:
        try:
            stock = yfinance.Ticker(symbol)
        except Exception as e: 
            print(e)
    return stock
    
def printDictForConsole(myDict : dict, mysep="")->None:
    for key,value in myDict.items():
        print(key,mysep,value)
    
def filter(input:dict, filterKeys:Iterable) -> dict:
    result ={} 
    for i in filterKeys:
        result[i] = input[i]
    return result

def printMainInfos(myDict: dict)->None: 
    subKeys = ('symbol','shortName','sector','currency','country','sharesOutstanding','website','longBusinessSummary')
    #subDict = myDict.fromkeys(subKeys)
    subDict = filter(myDict,subKeys)
    printDictForConsole(subDict,": \n\t")

