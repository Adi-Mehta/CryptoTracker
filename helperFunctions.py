import os
import dash
import sqlite3
import plotly.graph_objs as go
import dash_core_components as dcc
import dash_html_components as html


def dfSort(df, curr):
    """Creates DB of just 1 crpyto"""
    return df[df.Name==curr]

def joinDBpath(selfName, dbName):
    """Connects DB and returns db path"""
    BASE_DIR = os.path.dirname(os.path.abspath(selfName))  #directory to get to DB
    db_path = os.path.join(BASE_DIR, dbName)    #db path
    return db_path

def returnCursor(fileName,dbName):
    """Returns cursor"""
    connection= sqlite3.connect(joinDBpath(fileName,dbName))
    curs = connection.cursor()
    return curs

def selectData(cursor):
    """
    Returns a tuple of crypto data (Name, Price, Date)
    """
    cursor.execute("SELECT * FROM Cryptos")
    rows = cursor.fetchall()
    return rows

def categorySort(list):
    return [list[i].pop(0) for i in range(len(list))], [list[i].pop(0) for i in range(len(list))], [list[i].pop(0) for i in range(len(list))], [list[i].pop(0) for i in range(len(list))],[list[i].pop(0) for i in range(len(list))]
    #NAMES -> PRICE -> Time -> rnk ->PRICe INC

def tracer(df, currencyName):
    return go.Scatter(y=(df['Price']), x=df.index,
                      hoverinfo = currencyName)

def dropDownTraces(df):
    return [tracer(dfSort(df,'bitcoin'),'Bitcoin'),tracer(dfSort(df,'ethereum'),'Ethereum'),tracer(dfSort(df,'litecoin'),'Litecoin'),tracer(dfSort(df,'Ripple'),'ripple')]

def dashBoard(df,currencyName):
    app = dash.Dash()
    app.layout = html.Div([
        dcc.Graph(
            id = 'Crypto-Data',
            figure = {
                'data': go.Scatter(y=(df['Price']),
                                   x=df.index),
                'layout': go.Layout(
                    xaxis = dict(
                        showgrid = True,
                        showline = True,
                        title = 'Date/Time'
                    ),
                    yaxis = dict(
                        showgrid = True
                    )
                )
            }
        )
    ])
    if __name__ == '__main__':
        app.run_server(debug=True)