import requests
import json
from concurrent.futures import ThreadPoolExecutor
import time
from datetime import datetime


NUMBER_OF_REQUESTS = 1000
LOG_FILE = "./layer7_http_flood.log"


def send_request():
    try:
        url = 'http://10.200.56.78/add-task' 

        data = {
            'task_name': 'Test Task',
            'task_description': 'This is a test task for load testing'
        }
        headers = {'Content-Type': 'application/json'}

        # response = requests.get(url=url)
        response = requests.post(url, data=json.dumps(data), headers=headers)
        
        # with open(LOG_FILE, 'a') as f:
        #     timestamp = datetime.now()
        #     f.write(f"[{timestamp}] {response.status_code} {response.text}")

    except Exception as e:
        pass
        # with open(LOG_FILE, 'a') as f:
        #     timestamp = datetime.now()
        #     f.write(f"[{timestamp}] Error: {e}\n")


def simulate_attack():
    with ThreadPoolExecutor(max_workers=NUMBER_OF_REQUESTS//100) as executor:
        for _ in range(NUMBER_OF_REQUESTS):
        # while (True):
            executor.submit(send_request)
        print(f"Done sending {NUMBER_OF_REQUESTS} POST requests!")



if __name__ == '__main__':
    start_time = time.time()
    simulate_attack()
    end_time = time.time()
    print(f"The process took {end_time - start_time} seconds")
