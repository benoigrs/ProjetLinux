import dash
from dash import Dash, dcc, html, Output, Input
import plotly.graph_objs as go

with open('value.txt', 'r') as f:
    values = f.readlines()

current = values[-1]

x_values = list(range(len(values) - 1))
y_values = [float(val.strip()) for val in values[:-1]]


app = dash.Dash(__Projet__)

app.layout = html.Div([
    html.H1('Pernod Ricard Stock'),
    html.H2('Current: {}'.format(current.strip()), style={'font-size': '40px'}),
    dcc.Graph(
        id='value-graph',
        figure={
            'data': [
                {'x': x_values, 'y': y_values, 'type': 'line'}
            ],
            'layout': {
                'title': 'Historical values',
                'xaxis': {'title': 'Time'},
                'yaxis': {'title': 'Value'}
            }
        }
    )
])


if __name__ == '__Projet__':
    app.run_server(debug=True,host="0.0.0.0",port="8050")
