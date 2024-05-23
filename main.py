from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import csv

datacsv = "./data.csv"
data = []


app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])

#fix this function so graph works
def datexsalesy():
    df=pd.read_csv('./data.csv')
    df = df.to_dict()

    for row in df:
        print(row)
        data.append([row['Item'],row['Date']])


        

@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    datexsalesy()
    df = pd.read_csv('./data.csv') # replace with your own data source

    x = 'Sales'
    y = 'Date'
    fig = px.line(df, x=x, y=y)
    return fig


app.run_server(debug=True)