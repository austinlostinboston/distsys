#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool
import os

## Import distsys
from distsys.services import services
## Collect command line arguments
try:
    dir_name = str(sys.argv[1])
except:
    dir_name = 'poop'
    print "You must enter a specific path for the new directory."


def create_dir(ip_addr):
    ## Get's current working directory and removes actions from the path
    file_dir = os.path.dirname(os.path.abspath(__file__)).replace('actions','')

    try:
        content = open(file_dir + 'config/config.ini','r')
        lines = content.read().split("\n")
        print lines
        usr_pwd = [line.split(" ") for line in lines]
        username = usr_pwd[0][1]
        password = usr_pwd[1][1]

        os.system('echo ' + password + ' | ssh ' + str(username) + '@' + str(ip_addr) + ';\'ls\'')

    except:
        print "Error reading config.ini file"


if __name__ == "__main__":
    s = services(localhost=False)
    num_clients = len(s.clients)

    print "Creating directory on clients"
    pool = Pool(processes=num_clients)
    pool.map(create_dir, s.clients)
    print "finished...no errors."