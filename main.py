import pandas
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
    dcc.Graph(id="graph"),
])

def noofsalesoverdate():
    ax = 'Date'
    ay = 'NoOfSales'
    dates=set([row['Date'] for row in data])
    header=(ax,ay)
    #subject to change based on the two values, currently date has to be x so we cannot just switch them over to fix .to_datetime() method
    newdata = {
        ay: [],
        ax: []
    }
    df = pandas.DataFrame(newdata)
    for date in dates:
        sub_list=[]
        for row in data:
            if row['Date']==date:
                sub_list.append(row)
        newrow = [str(len(sub_list)),date]
        df.loc[len(df)] = newrow
# order the dates
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date', ascending=True)
    return ax, ay,df



        

@app.callback(
    Output('graph', 'figure'),
    Input('button', 'value'))
def display_graph(value):
    datandaxis = noofsalesoverdate()
    fig = px.line(datandaxis[2], x=datandaxis[0], y=
                  datandaxis[1])
    return fig


app.run_server(debug=True)