#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool
import os

## Import distsys
from distsys.services import services
from distsys.statistics import mkdir

## Collect command line arguments
try:
    path = str(sys.argv[1])
    dir_name = str(sys.argv[2])
except:
    print "mkdir requires 2 arguments"
    print "arg 1 - path for new directory"
    print "arg 2 - name for new directory"
    sys.exit()


def create_dir(ip_addr):
    try:
        #os.system('ssh -T ' + str(ip_addr) + ';\'ls\'')
        mkdir(ip_addr, path, dir_name)
    except:
        print "Error reading config.ini file"


if __name__ == "__main__":
    s = services(localhost=False)
    num_clients = len(s.clients)

    print "Creating directory on clients..."
    pool = Pool(processes=num_clients)
    pool.map(create_dir, s.clients)
    print "finished..."