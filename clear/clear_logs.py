import redis

# Another useless python script to clear all the logs in the project at once.
LOG_FILES = ["../attacker/layer7_http_flood.log", "../webserver/gunicorn/gunicorn.log", "../webserver/requests.log", "../webserver/redis/redis.log", "../webserver/nginx/nginx.log", "../webserver/nginx/nginx.access.log", "../webserver/nginx/nginx.pid", "../webserver/gunicorn/gunicorn_access.log"]

for file in LOG_FILES:
    with open(file, 'w') as f:
        f.write("")

print("Cleared all the logs in the project present.")

r = redis.StrictRedis(host='localhost', port=6379, db=0)
r.flushall()
print("Clearing redis memory for the webserver.")