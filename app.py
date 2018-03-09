import coinmarketcap
import simplejson as json
import pandas as pd
import time
from pandas import Series, DataFrame
import datetime
import sqlite3

connection = sqlite3.connect("dataWrank.db")
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Cryptos (name VARCHAR NOT NULL, price REAL NOT NULL, time DATE NOT NULL, rank INTEGER NOT NULL, percentInc24hrs Integer NOT NULL)")  # create table with these columns
market = coinmarketcap.Market()

dataList = market.ticker()

for currency in dataList:
    if (currency['name'] == "Bitcoin" or currency['name'] == "Litecoin" or currency['name'] == "Ethereum" or currency['name'] == "Ripple"):  # tracks 4 currencys that i wanted
        r = currency['rank']
        n = currency['id']
        p = currency['price_usd']
        d = (time.strftime("%D %H:%M", time.localtime(int(currency["last_updated"]))))
        inc = currency['percent_change_1h']
        c.execute('''INSERT INTO Cryptos ( name, price, time, rank, percentInc24hrs)VALUES(?,?,?,?,?)''', (n, p, d, r, inc))
        connection.commit()
    df = pd.read_sql_query("SELECT * FROM Cryptos", connection)
    print(df)

connection.close()