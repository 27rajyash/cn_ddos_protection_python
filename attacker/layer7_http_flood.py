import requests
import json
from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime


NUMBER_OF_REQUESTS = 10000
LOG_FILE = "./layer7_http_flood.log"

# Function to send a request
def send_request():
    try:
        url = 'http://localhost:8000/add-task'

        data = {
            'task_name': 'Test Task',
            'task_description': 'This is a test task for load testing'
        }
        headers = {'Content-Type': 'application/json'}

        # response = requests.get(url=url)
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        with open(LOG_FILE, 'a') as f:
            timestamp = datetime.now()
            f.write(f"[{timestamp}] {response.status_code} {response.text}")

    except Exception as e:
        with open(LOG_FILE, 'a') as f:
            timestamp = datetime.now()
            f.write(f"[{timestamp}] Error: {e}\n")


# Simulate multiple requests
def simulate_attack():
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=NUMBER_OF_REQUESTS) as executor:
        for _ in range(NUMBER_OF_REQUESTS):  # Number of requests to send
            executor.submit(send_request)
        print(f"Done sending {NUMBER_OF_REQUESTS} POST requests!")

    end_time = time.time()
    print(f"The process took {end_time - start_time} seconds")


if __name__ == '__main__':
    simulate_attack()
