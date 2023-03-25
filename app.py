import dash
from dash import Dash, dcc, html, Output, Input
import plotly.graph_objs as go
import time


file = 'value.txt'

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

def update_figure():
    current, data = read_value()
    latest = current.split(' ')[-1]
    return generate_figure(data), latest

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Pernod Ricard Stock'),
    html.H2(id='current-value', style={'font-size': '40px'}),
    dcc.Graph(
        id='value-graph',
        figure=generate_figure([]),
    ),
    html.Div([
        html.H2('Last day'),
        html.Pre(id='daily-value'),
    ], style={'position': 'absolute', 'top': '0', 'right': '0'}),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # 1 second
        n_intervals=0
    )
])

@app.callback(
    [Output('value-graph', 'figure'),
     Output('current-value', 'children'),
     Output('daily-value', 'children')],
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    figure, latest = update_figure()
    with open('daily.txt','r') as f:
        daily=f.read()
    return figure, f'Current: {latest}', daily

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port="8050", threaded=True)
