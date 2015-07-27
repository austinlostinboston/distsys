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
    dir_name = str(sys.argv[1])
except:
    dir_name = 'poop'
    print "You must enter a specific path for the new directory."


def create_dir(ip_addr):
    try:
        #os.system('ssh -T ' + str(ip_addr) + ';\'ls\'')
        mkdir(ip_addr)
    except:
        print "Error reading config.ini file"


if __name__ == "__main__":
    s = services(localhost=False)
    num_clients = len(s.clients)

    print "Creating directory on clients"
    pool = Pool(processes=num_clients)
    pool.map(create_dir, s.clients)
    print "finished...no errors."