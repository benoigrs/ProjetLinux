import dash
from dash import Dash, dcc, html, Output, Input
import plotly.graph_objs as go


file = 'value.txt'

with open('daily.txt','r') as f:
    daily=f.read()

def read_value():
    with open(file, 'r') as f:
        lines = f.readlines()
    current = lines[-1]
    data = []
    for line in lines:
        parts = line.strip().split(' ')
        time = parts[0]
        value = float(parts[1])
        data.append((time, value))
    return current, data

def generate_figure(data):
    x_values = [d[0] for d in data]
    y_values = [d[1] for d in data]
    return {
        'data': [
            {'x': x_values, 'y': y_values, 'type': 'line'}
        ],
        'layout': {
            'title': 'Historical values',
            'xaxis': {'title': 'Time'},
            'yaxis': {'title': 'Value'}
        }
    }
  
current, data = read_value()
latest = current.split(' ')[-1]

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Pernod Ricard Stock'),
    html.H2('Current: {}'.format(latest), style={'font-size': '40px'}),
    dcc.Graph(
        id='value-graph',
        figure=generate_figure(data)
    ),
    html.Div([
        html.H2('Last day'),
        html.Pre(daily)
    ], style={'position': 'absolute', 'top': '0', 'right': '0'})
])

app.run_server(debug=True, host='0.0.0.0', port="8050")

