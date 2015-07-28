#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool 

## Import distsys
from distsys.services import services
from distsys.statistics import online


def client_status(client):
    if online(client):
        print "Client: " + str(client) + "\t" + "\033[92m" + "ON" + "\033[0m"
    else:
        print "Client: " + str(client) + "\t" + "\033[91m" + "OFF" + "\033[0m"

if __name__ == "__main__":
    s = services(localhost=False)
    num_clients = len(s.clients)

    print "Determining online status of clients..."
    pool = Pool(processes=num_clients)
    pool.map(client_status, s.clients)
