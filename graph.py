import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import tinydb

with open('priceData.db', 'w') as f:
    data =

"""
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(
        id='CryptocurrencyPriceData',
        figure={
            'data':[
                go.Scatter(
                    x='fetch date'
                    y='fetch price'
                )
            ]
        }
    )
])
"""