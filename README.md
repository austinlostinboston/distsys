# distsys
Distsys is a light weight, simple approach to setting up and interacting with a distributed system.
This code was originally written to control data analysis jobs running across 10 HP Compaq 6500 running Ubuntu 12.04.5.
In theory, this should work on any unix based system. Not tested for windows.


The system has two modes, local and distributed.
Local mode is for testing the system and playing around with the syntax.
It's really meant to help me understand workflows of the system before implementing equivalent functionalities for distributed mode.
Currently, only local actions have been implemented.



### Installation
```
git clone git@github.com:austinlostinboston/distsys.git
cd distsys
pip install -r requirements.txt
python setup.py develop
```
develop should be used during development to avoid reinstalling the project after every change.

## Directions (Distributed Mode)

Currently, distsys does not run as service on both the server and clients.
It utilizes a number of builtin functions of the Linux operating system like 
Below are directions outlining how to use the system and it's different fuctionalities.
Before you start, please make sure that you've enabled passwordless ssh between your server (master) and your clients. There's currently no need to enable this between clients.

### Configure Clients
```
cd distsys/config
vim clients.conf

## clients.conf is where you specify client IP Addresses.
## This tells the server/master node where to start up
## services and where to connect with them.
## Lines starting with '#' will be ignored.
192.168.1.1
192.168.1.2
...
```
Please enter each client ip on a new line.

#### Current list of distributed mode commands.
##### Note: All commands are interact with clients in an asyncronous fashion.
- **status** - Determines the online status for each client.
- **mkdir** - Creates a directory on each client at a specific path
- **data** - Distributes .txt, .zip, and .gz files across the clients

### Status
```
python director.py status

output:
Determining online status of clients...
Client: 192.168.1.5     ON
Client: 192.168.1.10    ON
Client: 192.168.1.6     ON
...
```

The status command sends a Linux 'ping to each client defined in clients.conf. Each ping sends two packets of data. If both packets are received by the client, the client is considered to b ONLINE. If any of the packets are lost, the client is considered OFFLINE.  

## Directions (Local Mode)
### Configure Ports
```
cd distsys/config
vim port.conf

## port.conf is where you specify the port each local 
## client runs on. This file is only used in local mode.
## Lines starting with '#' will be ignored.
15001
15002
```
By default, this file is setup to run two clients on port 15001 and 15002.
Feel free to change this to desired port values above 8000.

### Start up clients
```
cd distsys
python director.py start_local
```
This will startup services on the ports specified in your port.conf file.
It is best to have a dedicated terminal for clients when running the system locally.

### ping clients
```
python director.py ping
```
In a different terminal from the clients, run the above command.
This sends a ping to each client service.
Each client then sends an echo back to the director node server.

### shutdown system
```
python director.py shutdown_local
```
This shutdowns the system processes running the as the clients.