import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send a request
def send_request():
    try:
        response = requests.get('http://localhost:8000/computational-work')
        print(response.status_code, response.text)
    except Exception as e:
        print(f"Error: {e}")

# Simulate multiple requests
def simulate_attack():
    with ThreadPoolExecutor(max_workers=200) as executor:
        for _ in range(200):  # Number of requests
            executor.submit(send_request)
        print("Done sending two hundred requests!")

if __name__ == '__main__':
    simulate_attack()