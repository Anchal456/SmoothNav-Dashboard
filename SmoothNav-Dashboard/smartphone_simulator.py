
import requests
import random
import time

url = 'http://localhost:5000/send-data'

while True:
    payload = {
        "gyroscope": [random.uniform(-1, 1) for _ in range(3)],
        "accelerometer": [random.uniform(-1, 1) for _ in range(3)],
        "magnetometer": [random.uniform(-1, 1) for _ in range(3)]
    }
    requests.post(url, json=payload)
    time.sleep(0.5)
