import os
import dash
from dash import dcc, html
from dash.dependencies import Output, Input
import plotly.graph_objs as go
import threading
from socketIO_client_nexus import SocketIO as ClientSocketIO

# Read SERVER_URL from environment variables (fallback to localhost)
server_url = os.getenv('SERVER_URL', 'http://localhost:5000')

# Store real-time data globally
latest_data = {"gyroscope": [0, 0, 0], "accelerometer": [0, 0, 0], "magnetometer": [0, 0, 0]}

# Background thread to listen to WebSocket
def start_socket_listener():
    def on_sensor_data(data):
        global latest_data
        latest_data = data

    client_socket = ClientSocketIO(server_url, 80)
    client_socket.on('sensor_data', on_sensor_data)
    client_socket.wait()

threading.Thread(target=start_socket_listener, daemon=True).start()

# Dash App setup
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H2('SmoothNav Sensor Visualization'),
    dcc.Graph(id='gyro-graph'),
    dcc.Graph(id='accel-graph'),
    dcc.Graph(id='magneto-graph'),
    dcc.Interval(id='interval-component', interval=500, n_intervals=0)
], style={'max-width': '600px', 'margin': 'auto'})

@app.callback(
    [Output('gyro-graph', 'figure'),
     Output('accel-graph', 'figure'),
     Output('magneto-graph', 'figure')],
    Input('interval-component', 'n_intervals')
)
def update_graph(n):
    gyro = latest_data['gyroscope']
    accel = latest_data['accelerometer']
    magneto = latest_data['magnetometer']

    gyro_fig = go.Figure(data=[go.Scatter3d(
        x=[0, gyro[0]],
        y=[0, gyro[1]],
        z=[0, gyro[2]],
        mode='lines+markers',
        marker=dict(size=5, color='red')
    )])
    gyro_fig.update_layout(title='Gyroscope')

    accel_fig = go.Figure(data=[go.Scatter3d(
        x=[0, accel[0]],
        y=[0, accel[1]],
        z=[0, accel[2]],
        mode='lines+markers',
        marker=dict(size=5, color='green')
    )])
    accel_fig.update_layout(title='Accelerometer')

    magneto_fig = go.Figure(data=[go.Scatter3d(
        x=[0, magneto[0]],
        y=[0, magneto[1]],
        z=[0, magneto[2]],
        mode='lines+markers',
        marker=dict(size=5, color='blue')
    )])
    magneto_fig.update_layout(title='Magnetometer')

    return gyro_fig, accel_fig, magneto_fig

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
