# distsys
Distsys is a light weight, simple approach to setting up and interacting with a distributed system.
This code was originally written to control data analysis jobs running across 10 HP Compaq 6500 running Ubuntu 12.04.5.
In theory, this should work on any unix based system. Not tested on windows.

### Installation
```
cd distsys
python setup.py install
```
or
```
git clone git@github.com:austinlostinboston/distsys.git
```

### Directions for use (Local Mode)
Start up system
```
cd distsys
python director.py start_local
```

ping clients
```
python director.py ping
```

shutdown system
```
python director.py shutdown_local
```