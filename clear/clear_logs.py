#Another useless python script to clear all the logs in the project at once.
LOG_FILES = ["../attacker/layer7_http_flood.log", "../webserver/gunicorn_error.log", "../webserver/requests.log"]

for file in LOG_FILES:
    with open(file, 'w') as f:
        f.write("")