
# SmoothNav 3D Visualization Dashboard

This project provides a real-time 3D visualization dashboard for SmoothNav ML prototype.

## 🧱 Components
- **server.py**: Receives data from smartphone and emits it via WebSocket.
- **dashboard.py**: Displays real-time 3D graphs using Dash.
- **smartphone_simulator.py**: Simulates sensor data and sends it to the server.

## ⚡ Run Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start the server:
   ```
   python server.py
   ```

3. Start the dashboard:
   ```
   python dashboard.py
   ```

4. Run the simulator (or replace with actual smartphone app):
   ```
   python smartphone_simulator.py
   ```

5. Open browser at `http://<SERVER_IP>:8050` (mobile-friendly).

## 🚀 Notes
- Replace `localhost` in the simulator and dashboard with your server IP when deploying.
