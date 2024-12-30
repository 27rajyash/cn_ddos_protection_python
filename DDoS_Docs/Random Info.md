- DDoS protection services are provided by companies like Cloudflare and AWS. Although functional they cost a lot of money to employ, rightfully so, I cannot imagine the amount of resources that they must have to provide event to route all the traffic through their reverse proxies.

- In computer networks, a ==reverse_proxy== or surrogate server is a proxy server that appears to any client to be an ordinary web server, but in reality merely acts as an intermediary that forwards the client's requests to one or more ordinary web servers

- venv is a python virtual environment that allows us to build dependencies for the project the venv folder is packaged in. It contains all the libraries required to run our current project without messing with the global repository of libraries in your device. This prevents any conflicts between the global version of a certain module and the version required to run the current project. 

- Usually web server is thread bound as in it does not allocate an unlimited number of threads for all incoming requests and only serves a certain number of requests at a time, then no matter how many requests you send number it is impossible to overwhelm the resources of a server using high number of requests, it will queue the requests until its buffer overflows and will drop further requests until its done with the requests in its buffer. In such cases the legitimate user anywhich ways can't get to the server ruining his experience. Also there are different types of bottlenecks including I/O and CPU, and CPU bottlenecks are hard to find in real life servers.

- Web servers in production usually use full-fledged DBMS system having complex configurations and features instead of file/document based database systems like SQLite. They are built for concurrent use, persistence and scalability. Funnily enough, MongoDB, a NoSQL DBMS system which uses .json 'document-like' formatting, is much more popular today because of the same features, simplicity and SPEED.

- The `app.run()` method in Flask is typically used for running the server in development mode. If you provide the `host` and `port` arguments, Flask will start the server on the specified address. But, in production (when using Gunicorn), this method is not used to run the server.

- Using the `limiter` library in python is extremely easy. You just add the following lines to initiate a limiter and apply it on a certain app route to apply it tothat.
	`limiter = Limiter(get_remote_address, app=app, default_limits=["200 per minute"])
	`@app.route('/endpoint', methods=['POST']) 
	`@limiter.limit("10 per second")`

- Wrappers and decorators are **essential tools in a Python developer's toolkit**. They provide a clean and elegant way to modify or extend the behavior of functions, without cluttering the core implementation.

	- A **wrapper** in Python refers to a function or method that "wraps" another function or object, adding additional functionality to it. Wrappers are often used to modify or extend the behavior of a function or object without changing its original implementation.
		  `def wrapper_function(original_function):`
			  `def wrapped_function(*args, **kwargs):`
				  `print("Wrapper: Before the function call.")`
				  `result = original_function(*args, **kwargs)`
				  `print("Wrapper: After the function call.")`
				  `return result`
			  `return wrapped_function`

	- A **decorator** is a specialized type of wrapper in Python. It's a syntactic feature that allows you to apply a wrapper function to another function in a concise way using the `@decorator_name` syntax.
		`def my_decorator(func):` 
			`def wrapper(*args, **kwargs):` 
				`print("Decorator: Before the function call.")` 
				`result = func(*args, **kwargs)` 
				`print("Decorator: After the function call.")` 
				`return result` `
			`return wrapper`
			
		`@my_decorator` `
		`def say_hello(name): 
			`print(f"Hello, {name}!")`

- In Python, locks are a synchronization mechanism used to control access to shared resources in a multi-threaded environment. They help prevent race conditions, where multiple threads try to access and modify the same data simultaneously, leading to unpredictable and incorrect results.
