import coinmarketcap
import simplejson as json
import pandas as pd
import time
from pandas import Series, DataFrame
import datetime
import sqlite3

connection = sqlite3.connect("priceData.db")
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Cryptos (name VARCHAR NOT NULL, price REAL NOT NULL, time DATE NOT NULL)")

market = coinmarketcap.Market()
currencies=["bitcoin", "ethereum", "litecoin", "ripple"]


for currency in currencies:
    data = pd.DataFrame(market.ticker(currency))
    n= data.get('name').iloc[0]
    p = data.get('price_usd').iloc[0]
    d=datetime.datetime.fromtimestamp(int(data.get('last_updated').iloc[0])).strftime('%Y-%m-%d %H:%M:%S')
    c.execute('''INSERT INTO Cryptos ( name, price, time)VALUES(?,?,?)''', (n, p, d))
    connection.commit()

c.execute("SELECT name FROM Cryptos")

rows = c.fetchall()

c.close()
connection.close()