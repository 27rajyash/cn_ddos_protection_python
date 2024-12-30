import time
from functools import wraps
from flask import request, jsonify

import logging

LOG_FILE = "./requests.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')
def log_request(requester_ip: str, request_type: str):
    logging.info(f"IP: {requester_ip}, Request_type: {request_type}")


request_data = {}

def limit_rate(max_requests: int, window_size: int):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            client_ip = request.remote_addr
            current_time = time.time()
            
            if client_ip not in request_data:
                request_data[client_ip] = {"count": 0, "start_time": current_time}
            
            data = request_data[client_ip]
            elapsed_time = current_time - data["start_time"]
        
            if elapsed_time > window_size:
                request_data[client_ip] = {"count": 1, "start_time": current_time}
            
            else:
                if data["count"] >= max_requests:
                    return jsonify({"error": "Too many requests"}), 429
                request_data[client_ip]["count"] += 1


            return f(*args, **kwargs)
        return wrapped
    return decorator