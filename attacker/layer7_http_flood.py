import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send a request
def send_request():
    try:
        response = requests.get('http://localhost:8000/heavy-task')
        print(response.status_code, response.text)
    except Exception as e:
        print(f"Error: {e}")

# Simulate multiple requests
def simulate_attack():
    with ThreadPoolExecutor(max_workers=1000) as executor:
        for _ in range(1000):  # Number of requests
            executor.submit(send_request)
        print("Done sending a thousand requests!")

if __name__ == '__main__':
    simulate_attack()
