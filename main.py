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
    dcc.Graph(id="graph"),
    dcc.RadioItems([
                {
            'label':html.Div(['Item Over Total Spending'], style={'color': 'Black', 'font-size': 15, 'display' : 'inline-block', 'font-family' : 'Arial','width' : '15%', 'margin': 'none', 'padding' : '10px' }),
            "value": "itemovertotalspending"
        },
        {
            'label':html.Div(['Item Over Quantity Purchased'], style={'color': 'Black', 'font-size': 15, 'display' : 'inline-block', 'font-family' : 'Arial','width' : '15%', 'margin': 'none', 'padding' : '10px' }),
            "value": "itemoverquantity"
        },
        {
            'label':html.Div(['NoOfSales Over Date'], style={'color': 'Black', 'font-size': 15, 'display' : 'inline-block', 'font-family' : 'Arial','width' : '15%', 'margin': 'none', 'padding' : '10px' }),
            "value": "noofbuysoverdate"
        }],value='itemovertotalspending',  id='radio-button-picker')])

def noofsalesoverdate():
    ax = 'Date'
    ay = 'NoOfItemsBought'
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

    df = pd.to_datetime(df['Date'])
    print(df)
    return ax, ay,df

def itemoverquantity():
    ax = 'Item'
    ay = 'Quantity'
    #subject to change based on the two values, currently item is x so its easy
    newdata = {
        ax: [],
        ay: []
    }
    df = pandas.DataFrame(newdata)
    for row in data:
         newrow=row[ax],row[ay]
         df.loc[len(df)] = newrow
    df = df.sort_values('Quantity', ascending=False)
    return ax, ay,df

def itemovertotalprice():
    ax = 'Item'
    ay = 'Total Spending'
    names=set([row['Item'] for row in data])
    header=(ax,ay)
    #subject to change based on the two values, currently date has to be x so we cannot just switch them over to fix .to_datetime() method
    newdata = {
        ax: [],
        ay: []
    }
    df = pandas.DataFrame(newdata)
    for name in names:
        sub_value=0
        for row in data:
            if row['Item']==name and row['Comment']!= 'Multiorder':
                sub_value = sub_value+row['Price']
        
        df.loc[len(df)] = name,sub_value
    return ax, ay,df


@app.callback(
    Output('graph', 'figure'),
    Input('radio-button-picker', 'value'))
def display_graph(value):
    if value=='itemoverquantity':
        datandaxis = itemoverquantity()
        fig = px.bar(datandaxis[2], x=datandaxis[0], y=
                datandaxis[1], width=2400, height=1000)
    elif value=='noofbuysoverdate':
        datandaxis = noofsalesoverdate()
        fig = px.line(datandaxis[2], x=datandaxis[1], y=
                datandaxis[0],  width=2400, height=1000)
        
    elif value=='itemovertotalspending':
        datandaxis = itemovertotalprice()
        fig = px.bar(datandaxis[2], x=datandaxis[0], y=
                datandaxis[1],  width=2400, height=1000)
    
    fig.update_layout(
        font_family="Arial",
        font_color="Black",
        font_size=15,
        title_font_family="Arial",
        title_font_color="black",
        title_font_size=30
    )

    return fig

if __name__ == '__main__':
    app.run(debug=True)