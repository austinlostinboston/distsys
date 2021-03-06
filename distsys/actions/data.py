#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool, Value
import os

## Import distsys
from distsys.services import services
from distsys.statistics import online
from distsys.data import distribute_data, mkdir, checksumClient, checksumServer, rm_local
from distsys.utils import getFileName

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
        fName = getFileName(f)

        ## Increment num files transferred
        transfer.value += 1

        ## Get checksum of file from server
        svrChksum = checksumServer(f)
        
        ## Print copy status
        os.system('scp -q ' + f + ' ' + ip_addr + ':' + transfer_path)

        ## Get checksum of transferred file on client
        cltChksum = checksumClient(ip_addr, transfer_path + "/" + fName)

        ## If file's checksums are different, add to the failed variable
        if svrChksum != cltChksum:
            failed.value += 1
        else:
            ## Remove file if it passed checksum
            rm_local(f)
        
        ## Run checksum on client and return value
        sys.stdout.write("\rTransferred %d/%d files | %d files failed checksum..." % (transfer.value, total.value, failed.value))
        sys.stdout.flush()

## Setup function to set global variables for shared state
def setup(to, tr, fail):
    global total
    global transfer
    global failed
    total = to
    transfer = tr
    failed = fail

if __name__ == "__main__":
    ## Get client ips
    s = services(localhost=False)
    num_clients = len(s.clients)

    client_files, total = distribute_data(num_clients, path)

    ## Setup shared state variable
    total_files = Value('i', total)
    transfer_files = Value('i', 0)
    failed_files = Value('i', 0)

    combo = []
    for i in range(num_clients):
        combo.append([s.clients[i],client_files[i]])

    print "Distributing data..."
    pool = Pool(processes=num_clients, initializer=setup, initargs=[total_files, transfer_files, failed_files])
    pool.map(transfer_data, combo)
    print "\033[92m" + "transfer complete!" + "\033[0m\n"
