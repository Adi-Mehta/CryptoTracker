from helperFunctions import categorySort, selectData, joinDBpath
import sqlite3
import dash
import plotly.plotly as py
from plotly.graph_objs import *
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

connection = sqlite3.connect(joinDBpath('board.py', 'dataWrank.db'))    #gathers table made in tracker
cursor = connection.cursor()
app = dash.Dash()

rows = [list(row) for row in selectData(cursor)] #changes from tuple to list
nameRow, priceRow, timeRow, rankRow, priceIncRow = categorySort(rows)    #sorts rows by category

prices = [str(i).split(',') for i in priceRow]    #PRICE LIST of lists

dataFrame = pd.DataFrame(data ={'Name':nameRow,'Price':prices}, index=timeRow) #creates initial DataFrame
#print(list(dataFrame.index))

trace1 = {
    "x": list(dataFrame.index.values),
    "y":list(dataFrame['Price']),
    "connectgaps": False,
    "hoverinfo": "x+y+text",
    "line": {"width": 2},
    "marker":
    {
        "autocolorscale": False,
        "cauto": True,
        "cmax": 8,
        "cmin": 2,
        "showscale": False,
        "size": 5,
        "sizemode": "area",
        "sizeref": 0.00625,
    },
    "mode": "markers",
    "name": "price",
    "showlegend": True,
    "text": list(dataFrame['Name']),
    "type": "scatter",
}
data = Data([trace1])
layout = {
    "autosize": True,
    "dragmode": "pan",
    "font": {
        "family": "Overpass",
        "size": 12
    },
    "hovermode": "closest",
    "legend": {"borderwidth": -1},
    "paper_bgcolor": "rgb(198, 236, 227)",
    "showlegend": True,
    "title": "Crypto Currency Prices",
    "titlefont": {
        "family": "Overpass",
        "size": 22
    },
    "xaxis": {
        "autorange": False,
        "dtick": 13,
        "exponentformat": "none",
        "nticks": 9,
        "range": [-8.83020955585, 198.083576367],
        "showticklabels": True,
        "tick0": 0,
        "tickfont": {"family": "Overpass"},
        "tickmode": "linear",
        "ticks": "",
        "title": "time",
        "titlefont": {
            "family": "Overpass",
            "size": 15
        },
        "type": "category"
    },
    "yaxis": {
        "autorange": False,
        "range": [-506.733900001, 6938.39983074],
        "title": "price",
        "type": "linear"
    }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)


"""
app.layout = html.Div([
    html.H1('CryptoCurrency Data'),
    dcc.Dropdown(
        id='currencySelect',
        options=[
            {'label': 'Bitcoin', 'value': 'Bitcoin'},
            {'label': 'Ethereum', 'value': 'Ethereum'},
            {'label': 'Litecoin', 'value': 'Litecoin'},
            {'label': 'Ripple', 'value':'Ripple'}
        ],
        value='Bitcoin'
    ),
    dcc.Graph(id='my-graph')
])

@app.callback(Output('my-graph', 'figure'), [Input('currencySelect', 'value')])
def update_graph(selectedCurrency):
    df = dfSort(dataFrame, selectedCurrency)
    return {
        'data': tracer(df, selectedCurrency)
    }

if __name__ == '__main__':
    app.run_server()"""
cursor,connection.close()    #closes connection