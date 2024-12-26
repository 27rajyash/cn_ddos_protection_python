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
	#Terminal1
	`cd attacker`
	`source attacker_venv\bin\activate`
	`python layer7_http_flood.py`

Okay after the initial testing, I did run all of this all good and fine but when i run the server in one terminal and the attacker in another, what happens is all 1000 requests have been sent by the attacking script before i start getting the first response, I get the appropriate response for a while but then i start receiving this error messages that the connection was forcibly closed. After that all hell breaks lose and I start seeing timeouts and maximum retries exceeded errors. Now this is good sign saying the program works. However in all of this, the purpose of this test is never served, as in my CPU usage barely goes above 15%, memory usage stays stable and since i'm doing all of this on localhost, there is not point in checking the network usage.

Now the reason for this is the flask server doesn't have enough threads to handle these many requests and it quickly gets overwhelmed. Flask is not made for optimized, high-concurrency test. Maybe I'm not making the server do a more CPU intensive task. I also get connection request timeout because of the inherent bottleneck at localhost. Localhost uses the system's loop-back network interface, which is fast but can hit OS-level connection limits (e.g., max simultaneous open sockets). While the attacking script sends requests rapidly, each thread waits for the server's response, meaning they're effectively throttled by the server's slow processing.

What's the fix: I have to use Gunicorn which is a production-grade web server for flask to handle high concurrency. Also I have to increase OS level system resource limits to handle large number of connections.

BUT, all of this is for tomorrow,  I'm gonna make my commit for today and get to the other stuff I have pending... (See you tomorrow Rajjo!)
