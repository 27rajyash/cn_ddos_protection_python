DDoS (Distributed Denial of Service)

**What is DDoS?**:
Malicious attacker attacks a server using a network of compromised hosts to deny service to legitimate users of the said server.

_Malhar: Since for this project, we do not have a flurry of hosts to test the attacker from, we'll try to use as many devices we have at disposal and try to make it work. More like a DoS than a DDoS attack._ 

DDoS attack may last multiple days (The longest record is 38 days.)

**Recent Trends:**
The DDoS is a serious attack to business since major business may lose millions of dollars because of one such attack.

The number of attacks in recent years are considerably larger than that in the past whereas the average duration has also increased.
e.g. GitHub in 2018 had 129.6 million packets per second. Whereas Imperva (Some company) client had to endure one with about 500 million packets per second in 2019.
The biggest DDoS attack in history btw.

In 2019 a company named A10 network had claimed to track approximately 20.3 million DDoS weapons (Compromised hosts).

_Malhar: This is a good opportunity for anyone to learn about these cyber-attacks since they are becoming more prevalent by the day. Good for us Rajjo!_

Most attacks are from Linux-based hosts.
Instigation inherently will always be a step ahead of the defending mitigation.

**Botnet Structure:**
The network of zombie hosts controlled by the hostile attacker is called as the botnet.
There are many examples of botnets, e.g. AgoBot, PhatBot, etc.

First, an attacker looks out for vulnerable and insecure host machines and takes control of them by inserting some malicious script.

A botnet usually consists of three components, namely, bot master, Command and Control (C&C) channel, and a large number of bots. 

The C&C channel can made using any protocol, e.g. HTTP, TCP, UDP, etc.

Three types of botnet architectures:
	IRC (Internet Relay Chat)
		Nodes (hosts) are connected in a tree like structure. The root relays information to n closest nodes, those nodes relay the information to n nodes connected to them and so on...
	P2P (Peer to Peer):
		Nodes (hosts) are connected in a graph like structure, each node receiving as well as giving information to the nodes it is connected to.  
	HTTP (Hypertext Transfer Protocol):
		Centralized structure where each node (host) is connected directly to the root which acts as a client-server paradigm.

![[Comparison of botnet structures.png]]
Hybrid Architectures also exist like HTTPP2P hybrid architecture.
_Malhar: This is very similar to our (Mine and Suyog's CN project (Centralized P2P architecture).)_


## Types of DDoS attacks:

- **Voluminous or flooding attack**:
	In this attack, dummy data requests are generated in ample amount from 	multiple distributed sources and directed towards a specific node. The main motive of an attacker is to deplete the bandwidth of the targeted node. 
	
- **Protocol-based attack**:
	In protocol-based 	attack, the attackers take advantage of these vulnerabilities to perform a DDoS attack. They tend to exploit mainly layers 3 and 4 protocols to exhaust the processing capabilities and memory of the target node. 
	
- **Application layer attack**:
	This attack targets the seventh layer of the OSI reference model by obfuscating the web applications. Most persistent attacks nowadays.

![[Types of DDoS attacks.canvas|Types of DDoS attacks]]
Classification based on degree of automation:
	Manual Attack
	Semi-automatic Attack
	Automatic Attack

Classification based on Vulnerability Exploited:
	Volumetric Attack
	Amplification Attack
	Deformed Packet Attack
	Protocol Based Attack
_Malhar: Probably this is the best way to classify these attacks._

### Attack Tools
Freely available software:

| Tool         | Attack type                 |
| ------------ | --------------------------- |
| Mstream      | TCP SYN                     |
| Trinoo       | UDP FLooding                |
| HOIC         | HTTP Flooding               |
| XOIC         | HTTP/ICMP/TCP/UDP Flooding  |
| LOIC         | HTTP/TCP/UDP Flooding       |
| Tribe Flood  | Smurf/TCP/UDP/ICMP Flooding |
| HULK         | -\|\|-                      |
| Stacheldraht | -\|\|-                      |
| Knight       | -\|\|-                      |
| DDoSim       | -\|\|-                      |
| PyLoris      | Slowloris                   |
_Malhar: Need to check out the pyloris thing, since we are using python, it might be useful._

## Challenges in DDoS defense mechanisms.

- Distributed response:
	A DDoS defensive mechanism is required that can generate response from multiple scattered points of a network which should be generated cooperatively. Since the Internet is operated in a distributed environment, hence there is no enforcement or guarantee of wide deployment of any defense system or even cooperation between
	the networks.
	
- Lack of information sharing practice:
	Organisations do not exercise information sharing practice. Various parameters like  attack rate, duration, size of botnet, packet size, type of counter-response generated, its effectiveness type of damage, etc. are required to design a robust and holistic DDoS defensive mechanism. 
	
- Lack of Large-scale Testing:
	Organisations and researchers lack real-time environment to validate their respective mechanisms owing to the unavailability of large-scale test beds, secure methods
	of performing live remote trials over the Internet, or comprehensive and real-time-based simulation software that can sustain thousand nodes. 
	
- Lack of standardization and benchmarks
	Currently, there is no standard set for attack scenarios or verified, or documented evaluation framework that can allow comparison between the defense systems.
	
- Economic Factors:
	Parties that do not sustain direct harm from the DDoS attack must deploy a coordinated response system. It suggests an odd economic paradigm, since parties that endure the deployment expenses are not the parties that benefit directly from the scheme. 

## Classification of DDoS defense mechanisms. 

_Malhar: The following diagram gives us all the things we must/can implement._
![[Taxonomy of DDoS Defensive Mechanisms.canvas|Taxonomy of DDoS Defensive Mechanisms]]

**Classification Based on Methodology used**:

- Soft computing-based solutions
	To combat DDoS threats, soft computation approaches make the use of neural networks, genetic algorithms, Bayesian networks, fuzzy logic, etc. Soft computing systems can withstand inconsistencies and flaws.
	
- Statistical-based solutions
	In statistical-based solutions, regular statistical values for the normal traffic flow are computed. Subsequently, statistical values of current traffic are contrasted with those of the normative values to check maliciousness of the actual traffic flow. 
	
- Machine learning-based solutions:
	There is a need to train the security framework with attack-free data traffic in machine learning-based systems. Afterwards, the trained framework classifies attack traffic as destructive or legitimate. The most widely used approaches to DDoS attacks are machine learning-based solutions.
	
- Knowledge-based solutions


**Classification Based on Deployment Point: 

- Near to source-based solutions:
	In this section, we address defense mechanisms that are implemented near the origin of the attacks. These defensive processes are centralized in nature. Centralized points to the belief that mechanism-led defensive action only takes place at a basic hub in a network. It is the best practice to stop attack at its initial stage and prevent the malicious data traffic from disseminating into the network. 

	The sources of attack traffic are scattered (distributed) across the network, and
	data traffic from a single source is not significant enough for local Internet service provider (ISP) or local security systems to track. Therefore, it is not feasible to deploy defensive mechanism to monitor every node in the network.

- Near to destination-based solutions:
	Likely, close to source-based defensive mechanisms, these defensive mechanisms cannot properly filter off attack traffic as attack traffic is heavily regulated at the victim network boundaries. Being so in pro-active mode or in filtering, there is always some malicious traffic that reached the target server.

- Defensive mechanisms deploy-able at intermediate routers:
	These structures are typically implemented between the source and the destination at any intermediate routers. These types of solutions overcome the limitations of near to source or destination-based mechanisms. 

- Hybrid solutions:
	Hybrid solutions have distributed structures where different modules coordinate with each other to fight against any cyber-attack. Distributed defensive solutions are deployed across the Internet at different locations, and each entity functions according to its ability and cooperates with the other entities.

