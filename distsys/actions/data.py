#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool 
import os

## Import distsys
from distsys.services import services
from distsys.statistics import online
from distsys.data import distribute_data, mkdir

## Collect command line arguments
try:
    path = str(sys.argv[1])
    project = str(sys.argv[2])
except:
    print "data requires 2 arguments"
    print "arg 1 - path to the data"
    print "arg 2 - name for new directory"
    sys.exit()

def transfer_data(combo):
    ip_addr = combo[0]
    files = combo[1]

    ## Make project folder for data
    mkdir(ip_addr,'~/distsys/data/', project)

    ## Path files are transferred to
    transfer_path = '~/distsys/data/' + project

    for f in files:
        os.system('scp ' + f + ' ' + ip_addr + ':' + transfer_path)


if __name__ == "__main__":
    s = services(localhost=False)
    num_clients = len(s.clients)

    client_files = distribute_data(num_clients, path)
    combo = []
    for i in range(num_clients):
        combo.append([s.clients[i],client_files[i]])

    print "Distributing data..."
    pool = Pool(processes=num_clients)
    pool.map(transfer_data, combo)
