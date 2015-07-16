# distsys
Distsys is a light weight, simple approach to setting up and interacting with a distributed system.
This code was originally written to control data analysis jobs running across 10 HP Compaq 6500 running Ubuntu 12.04.5.
In theory, this should work on any unix based system. Not tested for windows.

### Installation
```
cd distsys
python setup.py install
```
or
```
git clone git@github.com:austinlostinboston/distsys.git
```

### Directions (Local Mode)
#### Configure Ports
```
cd distsys/config
vim port.conf
```
By default, this file is setup to run two clients on port 15001 and 15002.
Feel free to change this to desired port values above 8000.

#### Start up clients
```
cd distsys
python director.py start_local
```
This will startup services on the ports specified in your port.conf file.
It is best to have a dedicated terminal for clients when running the system locally.

#### ping clients
```
python director.py ping
```
In a different terminal from the clients, run the above command.
This sends a ping to each client service. Each client then sends an echo back to the director node server.

#### shutdown system
```
python director.py shutdown_local
```

### Directions (Distributed Mode)