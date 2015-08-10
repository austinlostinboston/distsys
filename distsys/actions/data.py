#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool, Value
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
        ## Increment num files transferred
        transfer.value += 1
        os.system('scp -q ' + f + ' ' + ip_addr + ':' + transfer_path)

        ## Print copy status
        print "Transferred: " + str(transfer.value) + "/" + str(total.value)

def setup(to, tr):
    global total
    global transfer
    total = to
    transfer = tr

if __name__ == "__main__":
    ## Get client ips
    s = services(localhost=False)
    num_clients = len(s.clients)

    client_files, total = distribute_data(num_clients, path)

    ## Setup shared state variable
    total_files = Value('i', total)
    transfer_files = Value('i', 0)

    combo = []
    for i in range(num_clients):
        combo.append([s.clients[i],client_files[i]])

    print "Distributing data..."
    pool = Pool(processes=num_clients, initializer=setup, initargs=[total_files, transfer_files])
    pool.map(transfer_data, combo)
