from dash import Dash, html, dcc, Input, Output
from datetime import time
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.read_csv('./data.csv')



df = df.reindex(index=df.index[::-1])
date = []

df['date'] = Date




app.layout =html.Div([
    dcc.Graph(id='graph',
              figure = {},
                 ),
    dcc.RadioItems(
    [
        {
            "label": html.Div(['All'], style={'color': 'Black', 'font-size': 25, 'display' : 'inline-block', 'font-family' : 'Verdana','width' : '10%', 'margin': 'auto', 'padding' : '10px'  }),
            "value": "all",
        }

    ], value='simple', inline = False, id = 'radio-button-picker'
)])


@app.callback(
    Output('graph', 'figure'),
    Input('radio-button-picker', 'value'))
def update_graph():
    df=df.copy()

    fig = px.line(dfr, x = 'date', y = 'sales', labels={
                     "date": "Date of Purchase",
                     "sales": "Sales(£)",
                 },
                title="Pink Morsel Sales - Soul Foods")

    fig.update_layout(
        font_family="Verdana",
        font_color="Black",
        font_size=15,
        title_font_family="Arial",
        title_font_color="black",
        title_font_size=30
    )

    return fig



if __name__ == '__main__':
    app.run_server(debug=True)

