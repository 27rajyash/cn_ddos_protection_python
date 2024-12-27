Python3:
	Python3 will be referred to as python from here on. Python does provide the programmer with a lot relaxation when it comes to memory management and simple syntax. Don't even get me started on the tons and TONS of libraries that it has. There is a reason why so many prefer this language in our college. Also, it is the only language we both know. 

Flask:
	Python (Since we are using python as the programming language, we have like three options: Flask, Django,) Library required to create a web server.
	Chose this library because very simple to understand and build. Even if need to add a backend and make it more complex, it will be much easier than say Django.
	It also will allow to create actual webserver with a GUI (website) to test our application on.

psutil:
	psutil (python system and process utilities) is a cross-platform library for retrieving information on running **processes** and **system utilization** (CPU, memory, disks, network, sensors) in **Python**. It is useful mainly for **system monitoring**, **profiling**, **limiting process resources** and the **management of running processes**. It implements many functionalities offered by UNIX command line tools such as: _ps, top, lsof, netstat, ifconfig, who, df, kill, free, nice, ionice, iostat, iotop, uptime, pidof, tty, taskset, pmap_.

matplotlib:
	matplotlib is a (really basic) library for creating static, animated, and interactive visualizations in Python.

gunicorn:
	Gunicorn is a WSGI HTTP server for Python web applications, including Django. It **serves as the interface between Django/Flask and the web, handling requests and passing them to Django for processing**. It uses multiple worker processes to handle concurrent requests, making it suitable for production environments. For a detailed description on how to use gunicorn, see [[Random Info]]. 
	
- gunicorn options:
1. **`--bind`**: Specify the host and port to bind to (e.g., `0.0.0.0:8000`).
2. **`--workers`**: Number of worker processes to handle requests.
4. **`--threads`**: Number of threads per worker (for threaded workers).
5. **`--timeout`**: Max seconds a worker can handle a request before being killed.
6. **`--daemon`**: Run Gunicorn in the background.
7. **`--access-logfile`**: File to log access requests.
8. **`--error-logfile`**: File to log errors.
9. **`--log-level`**: Set logging verbosity (`debug`, `info`, `warning`, etc.).
10. **`--keep-alive`**: Keep-alive timeout for HTTP connections.
11. **`--preload`**: Preload the app before workers are forked (reduces startup time).
12. **`--max-requests`**: Restart a worker after handling a specified number of requests.
13. **`--worker-connections`**: Max simultaneous clients for asynchronous workers.
14. **`--reload`**: Restart workers when code changes (useful in development).
15. **`--graceful-timeout`**: Timeout for graceful worker shutdown.
22. **`--config`**: Specify a configuration file for Gunicorn.
25. **`--check-config`**: Validate the configuration without starting the server.

reqwest:
	Requests is an Apache2 Licensed HTTP library, written in Python. The `requests` module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc).

mysql:
	MySQL is a popular open-source Database Management System (RDBMS) that uses SQL for database operations. While MySQL is a specific database system accessible for free and supports various programming languages. Reason to choose over something like PostgreSQL is that we already have experience with mysql and already have it on our computer. Using this over something like SQLite is that, this is a full-fledged DBMS that actual servers built for concurrency and frequent updates usually have. There is no reason to choose it over MongoDB, except its a completely different thing that we have to learn.

mysql-connector-python:
	MySQL Connector/Python is an API that allows Python programs to access MySQL databases.