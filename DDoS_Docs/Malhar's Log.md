re**This file is for me to log my progress. You don't have to read it thoroughly although I hope you do, but I totally understand if you don't since it is very long, I've noted down all the important info from this document in [[Random Info]], [[Dependencies]] and [[DDoS_Docs/Project Till Now]], read those instead. If you do get stuck up somewhere, I most likely have written about it in this document, or just ask me.** 

For now, the Fundamentals noted down in the Fundamentals folder are more than enough to get us started on the basic implementation. We will add more after we hit a resource exhaustion point.

 #Log1 {26-12-2024 [17:59:00]}

Okay, finally! I have to start implementing this project if we want to keep our deadline. IT's 26th December 1800 hours exactly (O __ O)!!

From all I've gathered from the accompanying book (which is only good for the fundamentals and not the actual implementation) and from the internet (and of course ChatGPT), there are three components of a DDoS Defense Mechanism, those being
	Detection
	Mitigation
	Prevention
For now I'm only focusing on the mitigation part. 

There are also different types of attacks (it is a bit overwhelming for the moment but I'm sure it will get simpler in the near future). For now just keep in mind that the most important and hard to detect is a HTTP flood attack. It's a voluminous or flood type of attack which works by occupying the bandwidth of the targeted web server with dummy HTTP requests (packets) so that the server either gets overwhelmed by consuming all its resources, crashing itself or its network bandwidth gets congested that the most legitimate requests are not served, thereby ruining user experience and costing the company that hosts the server millions (basically all DDoS attacks work in some way similar to this). Usually these HTTP requests are POST or a complex set of requests that requires larger number of packets as well as requires back-end processing by the web server. 

So my method of simulating this (attack) is not to create a full-fledged web server but rather create a simple, light-weight server using flask in python. I will create a script in python that also monitors the resources consumed by the server. Then I will create a script that sends repeated requests to the server which should end up consuming resources but since I'm only sending the packets from localhost to localhost, there is no way that I can create enough traffic to cause a bandwidth issue. At least we'll get to see the attack in action. Next step to this would be move the attacking script over to my other laptop or my phone and then trying to block bandwidth of the local network between my laptop and my phone.

I've created a sub-folder in the project folder named webserver that will have the HTTP web server and another sub-folder called the attacker for obvious reasons. In the webserver I have created a virtual environment called ==webs_venv==  to build the web-server in flask. I'm also monitoring resources and plotting them in real time using matplotlib using another script. Again, we don't have a botnet, so I'm implementing an layer 7 (application layer) HTTP flood DoS (not DDoS) attack. The way I'm making the server run a "heavy task" is that I'm bubble sorting an array of 2000 elements (1000 is too little I guess).

Keep in mind that there are different virtual environments for both the attacker as well as the server. For now you have to run three different scripts. 
First open the resource monitor in one terminal window after activating the venv:
	(Assuming you're in the project directory named cn_ddos_protection_python)
	#Terminal1
	`cd webserver`
	`source web_venv\bin\activate`
	`python resource_monitor.py`
Alternatively you can monitor the resources from your system manager (if you have one in your fucking macbook, looking at you Rajjo!)

Then run the web server in the same directory:
	(Assuming you're in the project directory named cn_ddos_protection_python)
	#Terminal2
	`cd webserver`
	`source web_venv\bin\activate`
	`python main.py`

Then run the attacker script in the attacker directory:
	(Assuming you're in the project directory named cn_ddos_protection_python)
	#Terminal3
	`cd attacker`
	`source attacker_venv\bin\activate`
	`python layer7_http_flood.py`

Okay after the initial testing, I did run all of this all good and fine but when i run the server in one terminal and the attacker in another, what happens is all 1000 requests have been sent by the attacking script before i start getting the first response, I get the appropriate response for a while but then i start receiving this error messages that the connection was forcibly closed. After that all hell breaks lose and I start seeing timeouts and maximum retries exceeded errors. Now this is good sign saying the program works. However in all of this, the purpose of this test is never served, as in my CPU usage barely goes above 15%, memory usage stays stable and since i'm doing all of this on localhost, there is not point in checking the network usage.

Now the reason for this is the flask server doesn't have enough threads to handle these many requests and it quickly gets overwhelmed. Flask is not made for optimized, high-concurrency test. Maybe I'm not making the server do a more CPU intensive task. I also get connection request timeout because of the inherent bottleneck at localhost. Localhost uses the system's loop-back network interface, which is fast but can hit OS-level connection limits (e.g., max simultaneous open sockets). While the attacking script sends requests rapidly, each thread waits for the server's response, meaning they're effectively throttled by the server's slow processing.

What's the fix: I have to use Gunicorn which is a production-grade web server for flask to handle high concurrency. Also I have to increase OS level system resource limits to handle large number of connections.

BUT, all of this is for tomorrow,  I'm gonna make my commit for today and get to the other stuff I have pending... 
(See you tomorrow Rajjo!)
{28-12-2024 [1:37:00]}

#Log2 {27-12-2024 [16:56:00]}

Okay! Time to implement those fixes we talked about yesterday.
I'm gonna first try to get gunicorn to work with my already existing program which I'm gonna install inside webserver venv.
Well that didn't take long, just installed it and works out of the box. 
Every single request sent on the webserver is appropriately served now. 
Now let's try some CPU intensive task and allowing greater bandwidth for the server.
Okay for CPU intensive task I'm trying to hash a short message a million times which I guess intensive load on the CPU (ChatGPT's suggestion). The bandwidth for the server I don't think requires much attention.

The gunicorn thing worked like magic. I'm currently employing 8 workers (8 separate threads) with the following command:

	gnicorn -c gunicorn_config.py main:web
	#This runs the web app from main.py file using the configuration options stored in the file gunicorn_config.py.

And I can already see improved performance, the CPU is being used at 80%, and none of the packets are dropped for the attacker.
Great! A new task is added to the list, to learn to use gunicorn. It is a great tool.

BUT this doesn't seem to work the way we expected, we expected as the number of requests sent on the web server increases, the more it consumes the resources of the server's processor and memory, and more effective the attack is and closer does the server get to crashing, however the usage in resources completely depends on the number of worker threads I choose to give to gunicorn. Admittedly, it did throttle the bandwidth, so much so that the thousandth request takes about a minute to complete. 

Okay a lot of information was gained in the last four minutes of web surfing asking the questions above. So, if a web server is thread bound as in it does not allocate an unlimited number of threads for all incoming requests and only serves a certain number of requests at a time, then no matter how many requests you send number it is impossible to overwhelm the resources of a server using high number of requests, it will queue the requests until its buffer overflows and will not accept anymore requests until its done with the requests at the moment. BUT apparently that is the point, in such cases the legitimate user anywhich ways can't get to the server ruining his experience. Also there are different types of bottlenecks including I/O and CPU, and CPU bottlenecks are hard to find in real life servers, so I might have to create a database in flask.

Okay I'm making some huge decisions for our project (sorry, Rajjo!), including choosing to use mysql. I have to download this shit, install and configure it. I also have to create a user in the server and a database specific for the project. This will be incredibly hard to get to work in your laptop. I will try to write a script that will automate this process.
Name of the database is 'ddos_webserver'
Name of the user is 'ddos_user'
Password for the user is 'ddos'

I had a question just now, we are specifying the host and port in both the flask script as well as the gunicorn_config.py file. I hope it won't get messed up if somehow they mismatch. ChatGPT clearifies:
The `app.run()` method in Flask is typically used for running the server in development mode. If you provide the `host` and `port` arguments, Flask will start the server on the specified address. But, in production (when using Gunicorn), this method is not used to run the server. 
I'll just remove fucking function then.

Okay, now we have a problem of having our databases aligned perfectly. My initial solution was to drop and recreate the table every time you run the server. But that shit too volatile man! Instead I've just created a sql file that will create a tasks table in mysql which we will be using on our web server btw, your automated script will handle that part for you too now.

With that, I'mma call it a day. It's 3:30 AM and my father is on the verge of beating me up if he finds me awake the next time he momentarily opens his eyes from his sleep. I'll make my daily commit now. On the agenda tomorrow is finishing the database and forward... Man I've really started to LOVE archlinux.

FUCK I JUST REALIZED I HAVEN'T DONE MY DAILY LEETCODE QUESTION!!!
(Bye!!)
{28-12-2024 [3:32:24]}


#Log3 {28-12-2024 [20:50:07]}

Fuck! I started very late today, although I was out for half of the day so...
Let's get started on that web server.
Man I love doing absolutely meaningless things instead of coding, like changing the font colour of comments and strings.

Reqwest does make our job easier to understand (not to implement since ChatGPT is carrying the heavy load).
Okay a lot of debugging in the mysql server later, we are finally able to connect to the database. (Few seconds later...) I guess not.

{(In Spongebob Squarepants voiceover) Few hours later...}
I wish I could kill myself. God why am I so stupid. I had downloaded the wrong sql server. Instead of mysql I had downloaded MariaDB which is a fork of mysql but not quite mysql.
Okay so there is no mysql package on the AUR or the pacman official repository. Apparently because mysql is proprietary (owned by oracle) and oracle being annoying doesn't help. Guess I gotta perform sacrilege as well now Also I gotta undo all the things that I did yesterday (requirements.txt and automation script).

https://www.reddit.com/r/archlinux/comments/s5ccq9/installing_mysql_not_mariadb_on_arch_linux/
This is very relevant post to my current problem.
https://www.reddit.com/r/archlinux/comments/s5ccq9/comment/kvp25q2/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
This comment is golden.

FINALLY! After a fuck ton of installations, configurations and debugging later which I can't bring myself to care about enough to write all of them down, our mysql backended server works with no problems... for now. Well it only has two functions, add a task and show tasks, so fuck it. This took too much time. Rest assured the code is self-explanatory. If you come across mysql installation, which I know you will, just ask me.

Somehow there are more tasks added than the attacker script intended. But that's for tomorrow morning (I promise!).
I'm calling it a day. I'm tired.
Bye Rajjo!
{29-12-2024 [12:28:08]}


#Log4 {29-12-2024 [11:49:07]}

I promised morning, and it is morning... Let's get this bitch started.

I've redirected the output of each script to a log file now. Also made a script in python to clear all those logs.
Okay right now I'm sending about twenty thousand http_flood requests and it takes about 39 seconds for server to serve all of them, the cpu_usage is pretty high at 98% max because of the 10 workers we're employing.

Now, first of all I'm concerned where the fuck Rajjo is and I'm skeptical that I'm doing the same thing that I did with Surlimar. I don't mind doing that, but it is very non-cooperative of me. 

Next thing I'll focus on implementing logging where the requests are coming from to my web server and then implementing a rate limiting method.
LOG EVERYTHING!!! NOTHING SHOULD BE PRINTED ON TERMINAL, EVERYTHING IN THE FUCKING BACKGROUND!!! (EVIL LAUGHTER) HAHAHAHAHAHAHA!!!!

Okay in order to implement the rate limiting method, we can go one of the two ways. One is the already present flask-limiter library or creating our own limiter, we'll try both but I'm inclined towards creating our own for now. That will show that we understand what rate-limiters are.
The rate limiter works. It wasn't much work honestly. Since we have limited each worker to about 100 requests, 10 worker allow about 1000 requests per minute.
I've also added graphical representation of how many requests from which IP. But the problem is it will visualize data since the server was started and I'm not sure I want to do that. Maybe only last minute are so.

God do I hate ChatGPT comments, explaining the most basic things possible.  


#Log4 {30-12-2024 [12:46:07]}

There was no outro for yesterday's log and I don't think that I'll be able to do much today either or tomorrow as a matter of fact because I have other stuff (Abhiyanta)!