#!/usr/bin/python

## Import builtins
import sys
from threading import Thread
from multiprocessing import Pool 

## Import distsys
from distsys.services import services
from distsys.statistics import online

s = services(localhost=False)
num_clients = len(s.clients)
#print s.clients

def client_status(client):
    if online(client):
        print "Client: " + str(client) + "\t" + "\033[92m" + "ON"
    else:
        print "Client: " + str(client) + "\t" + "\033[91m" + "OFF"

if __name__ == "__main__":
    print "Determining online status of clients..."
    pool = Pool(processes=num_clients)
    pool.map(client_status, s.clients)
