
from flask import Flask, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/send-data', methods=['POST'])
def receive_data():
    data = request.json
    socketio.emit('sensor_data', data)
    return {'status': 'success'}, 200

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
