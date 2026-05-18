import requests
import json
import pandas as pd
import mplfinance as mpl

url = 'https://api.mexc.com/api/v3/klines?symbol=BIT1USDT&interval=1m&limit=10' # tutaj należy umieścić adres url który zwraca jsona z danymi na temat świeczek (z poprzedniego zadania z Postmanem)
response = requests.get(url) # wywołanie to pobiera zasób znajdujący się pod danym adresem url 
responseBody = response.text # obiekt response zawiera atrybut "text", z naszymi danymi (całe response zawiera jeszcze dodatkowo metadane zapytania, które nie są nam potrzebne)
responseBodyJson = json.loads(responseBody)

formattedCandlesData = []
for item in responseBodyJson:
    formattedCandlesData.append({
        'time': int(item[0]), 
        'open': float(item[1]), 
        'close': float(item[4]), 
        'high': float(item[2]), 
        'low': float(item[3])
      })
    
print(responseBodyJson)
print(formattedCandlesData)

df = pd.json_normalize(formattedCandlesData)
df.time = pd.to_datetime(df.time, unit='ms')
df = df.set_index("time")

mpl.plot(
    df,
    type = "candle",
    title = "Candle chart",
    style = "yahoo",
    mav=(3,6,9)
)

    


