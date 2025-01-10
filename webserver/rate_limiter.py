import time
from functools import wraps
from flask import request, jsonify
import redis

import logging

LOG_FILE = "./requests.log"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')
def log_request(requester_ip: str, request_type: str):
    logging.info(f"IP: {requester_ip}, Request_type: {request_type}")


r = redis.StrictRedis(host='localhost', port=6379, db=0)
request_data = {}


def limit_rate(max_requests: int, window_size: int):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            client_ip = request.remote_addr
            current_time = time.time()
            key = f"rate_limit:{client_ip}"

            # Get the current request count and timestamp from Redis
            count, start_time = r.hmget(key, ["count", "start_time"])

            # If not found, initialize the values
            if count is None or start_time is None:
                r.hset(key, "count", 1)
                r.hset(key, "start_time", current_time)
            else:
                count = int(count)
                start_time = float(start_time)

                elapsed_time = current_time - start_time

                if elapsed_time > window_size:
                    # Reset the counter and start time if the window has passed
                    r.hset(key, "count", 1)
                    r.hset(key, "start_time", current_time)
                else:
                    if count >= max_requests:
                        return jsonify({"error": f"Too many requests from ip {client_ip}"}), 429
                    r.hincrby(key, "count", 1)

            return f(*args, **kwargs)
        return wrapped
    return decorator