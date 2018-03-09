import dash
import dash_core_components as dcc
import dash_html_components as html
import sqlite3
import plotly.graph_objs as go
import plotly.plotly as py
import pandas as pd
from helperFunctions import dfSort, joinDBpath, selectData, categorySort, dropDownTraces

timeRow = [] #needed to create index for graph
priceRow =[]
nameRow=[]
rankRow=[]
priceIncRow=[]

connection = sqlite3.connect(joinDBpath('graph.py', 'dataWrank.db'))    #gathers table made in tracker
cursor = connection.cursor()

rows = [list(row) for row in selectData(cursor)] #changes from tuple to list
"""print(rows)
s= cursor.execute("SELECT * FROM Cryptos")
r = cursor.fetchall()
for x in r:
    print(x)"""
nameRow, priceRow, timeRow, rankRow, priceIncRow = categorySort(rows)    #sorts rows by category

prices = [str(i).split(',') for i in priceRow]    #PRICE LIST of lists

dataFrame = pd.DataFrame(data ={'Name':nameRow,'Price':prices}, index=timeRow) #creates initial DataFrame

#for x in range(len(df)):
   # print(df[x])

#btcDf = dfSort(df,'bitcoin')    #creates sorted by currency data frame

#btcTrace= tracer(btcDf, 'Bitcoin')
#py.plot([btcTrace])    #plot


####START OF DASHBOARD APPLICATION####
"""traceData = dropDownTraces(df) #4 currencys tracer
updatemenus = list([
    dict(active =-1,buttons =list([
        dict(label = 'Bitcoin', method = 'update',
             args = [{'visible' : [True, True, False, False]}])
    ]))
])
"""
cursor,connection.close()    #closes connection


"""def dashBoard(df):
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(
            id='Crypto-Data',
            figure={
                'data': btcTrace,
                'layout': go.Layout(
                    xaxis=dict(
                        showgrid=True,
                        showline=True,
                        title='Date/Time'
                    ),
                    yaxis=dict(
                        showgrid=True
                    )
                )
            }
        )
    ])
    if __name__ == '__main__':
        app.run_server(debug=True)"""

#dashBoard(btcDf)