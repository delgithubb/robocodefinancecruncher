from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import csv

data = []
ax = ''
ay = ''
data = pd.read_csv('data.csv')
data = data.to_dict(orient='records')

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])

def noofsalesoverdate(ax,ay):
     ax = 'Date'
     ay = 'NoOfSales'
     dates=set([row['Date'] for row in data])
     header=[ay,ax]
     with open('datachange.csv', 'w') as output_file:
          csv.writer(output_file).writerow(header)
          for date in dates: 
               sub_list=[]
               for row in data:
                    if row['Date']==date:
                         sub_list.append(row)
               newrow = [str(len(sub_list)),date]
               csv.writer(output_file).writerow(newrow)
     return ax, ay
    




        

@app.callback(
    Output('graph', 'figure'),
    Input('button', 'value'))
def display_graph():
    datandaxis = noofsalesoverdate(ax,ay)
    df = pd.read_csv('./datachange.csv')
    fig = px.line(df, x=datandaxis[0], y=
                  datandaxis[1])
    return fig


app.run_server(debug=True)