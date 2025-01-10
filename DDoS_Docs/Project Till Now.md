I'm making this list as a note of what are our goals are at the moment, what we learned and what we need to learn in order to make this project successful. We will create separate lists that we will keep appending every time we learn about something new while implementing the project, so that the other can see what you've learned and keep up.

## Malhar
This is just for me, read it, don't edit it (-\_-)!
### Goal List
- [ ] To create a DDoS Defense Mechanism
	- [ ] To create a simple web server as our test subject.
		- [x] To Learn about Flask framework in python to implement a simple web server.
	- [ ] To create a DDoS attacker
		- [x] Setup separate virtual environments for the webserver and attacker.
		- [x] To create a simple Layer 7 HTTP flood attacker using python. 
			- [x] To Learn about Request HTTP library in python to send and request HTTP packets in the newer .json format for our attacker script.
	- [ ] To improve the web server to add features.
		- [x] Create a resource monitor script to constantly monitor the performance of the server including CPU usage, memory and network bandwidth.
		- [x] To learn about gunicorn and its configuration to run a production web page using python frameworks.
		- [x] To learn how to implement mysql databases in Flask framework in python.
		- [ ] Learn how to implement decorators and wrappers in python
	- [ ] Figure out a way to implement a DDoS attack using as few devices as possible.
		- [ ] To learn about Docker containers to safely run attacking scripts on my laptop. 
	- [ ] Add DDoS Detection, Prevention and Mitigation mechanisms.
		- [ ] Implement a log to track what requests come on the server and deploy a rate limiting method.
		- [ ]  Improve the rate limiter by running the webserver workers in asynchronous mode and sharing the same memory database.
- [ ] Make the project in accordance with good coding practices.
	- [ ] To create a shell script to automate the installation of mysql so anybody trying to fork this project has a better time. 
	- [ ] To learn how to write shell/batch scripts which will automate setting up our project.
	- [ ] To learn how to write tests and documentation.

#### Important Notes to Rajjo:
This is the section where I will write down all the (extremely, project-breaking/making) important one line information that has developed through my project building process.

- There is no point in making this project with the object-oriented model.

- I'm using mysql for the database on the web server. Please use the same on your laptop too (You kinda have to).
	Name of the database is 'ddos_webserver'
	Name of the user is 'ddos_user'
	Password for the user is 'ddos'
	There is only one table in the database named 'tasks'
	If you already have mysql, just run the file webserver_database.sql in the setup file. 

- We're not using the library flask-limiter to implement rate-limiter, we'll make our own.

- Instructions on what dependencies to download are in requirements.txt, they are instructions and not something for you to `pip install -r requirements.txt`. If you want to know what all these libraries are, I've written that in [[Dependencies]].

#### Instructions on how to run the project in its current state.

#Database_Setup
To setup the mysql server database and its user. (Only one time use!)
Before doing this make sure your mysql server service is running.
Open a terminal in the root directory of our project.
`cd setup`
`mysql -u ddos_user -p ddos_webserver`
`ddos`
`source ./webserver_database.sql`

#Run_Setup
Run the following commands in any terminal to start mysql and redis servers.
	`sudo systemctl start mysql` //Any terminal works fine.
	
#Terminal1 
To open the webserver. Before doing this make sure your mysql server service is running.
Open a terminal in the root directory of our project.
`cd webserver`
`source webs_venv/bin/activate`
`gunicorn -c gunicorn_config.py main:web`

#Terminal2 
To run the attacker script.
Open a terminal in the root directory of our project.
`cd attacker`
`python layer7_http_flood.py`


Nothing will be printed in the terminals (mostly), all the output is logged. Currently there are three different logs.
	- For the attacker output in the ./attacker folder
	- For the gunicorn service in the ./webserver folder
	- For the logging of incoming requests on the webserver in the ./webserver folder.

#clear
To clear all the logs.
Open a terminal in the root directory of our project.
`cd clear`
`python clear_logs.py`


To remove all the unnecessary tasks added to the ddos_webserver.
Open a terminal in the root directory of our project.
`cd clear`
`python clear_database.py`
