#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Process, Pool

## Import distsys
from distsys.services import services

## Startup service
local_service = services(localhost=True)
num_clients = len(local_service.clients)

## Create empty list of processes needed for service
procs = []
for client in local_service.clients:
    procs.append(None)

# Function of the client class method, needed for pooling
def start_clients(port):
    local_service.client(port)


if __name__ == "__main__":
    print "Starting " + str(num_clients) + " local clients..."
    pool = Pool(processes=num_clients)
    pool.map(start_clients, local_service.clients)
    #pool.apply_async(start_clients, local_service.clients, callback="finish")





