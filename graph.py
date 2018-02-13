import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import plotly.plotly as py
import pandas as pd
from helperFunctions import dfSort, joinDBpath, selectData, categorySort, tracer

timeRow = [] #needed to create index for graph
priceRow =[]
nameRow=[]

connection = sqlite3.connect(joinDBpath('graph.py', 'priceData.db'))
cursor = connection.cursor()

rows = [list(row) for row in selectData(cursor)] #changes from tuple to list

nameRow, priceRow, timeRow = categorySort(rows)    #sorts rows
prices = [str(i).split(',') for i in priceRow]    #PRICE LIST of lists

df = pd.DataFrame(data ={'Name':nameRow,'Price':prices}, index=timeRow) #creates initial DataFrame

btcDf = dfSort(df,'Bitcoin')    #creates sorted by currency data frame


btcTrace=tracer(btcDf, 'Bitcoin')
py.plot([btcTrace])    #plot

cursor,connection.close()    #closes connection"""