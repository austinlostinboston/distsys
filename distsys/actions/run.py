#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Pool
import os

## Import distsys
from distsys.services import services
from distsys.data import mkdir, remote_file_exists, distribute_data, run_script, collect_results

## Collect command line arguments
try:
    script_path = str(sys.argv[1])
    project_name = str(sys.argv[2])
except:
    print "data requires 2 arguments"
    print "arg 1 - path to distribute script/job"
    print "arg 2 - project name"
    sys.exit()

## Steps
#   Send script to each client
#   Execute script on client, send results to /output
#   Send files in output back to server

def run_job(combo):
    ip_addr = combo[0]
    local_script_path = combo[1][0]
    file_name = local_script_path.split("/")[-1]
    project_name = combo[2]

    client_script_path = "~/distsys/bin/" + project_name + "/" + file_name

    if remote_file_exists(ip_addr, client_script_path):
        pass
    else:
        os.system('scp ' + local_script_path + ' ' + ip_addr + ':' + client_script_path)

    run_script(ip_addr, client_script_path)

    collect_results(ip_addr, project_name)


if __name__ == "__main__":
    s = services(localhost=False)
    num_clients = len(s.clients)

    ## Distribute script only if it hasnt yet.    
    client_files = distribute_data(num_clients, script_path, job=True)

    combo = []
    for i in range(num_clients):
        combo.append([s.clients[i], client_files[i], project_name])

    print "Distributing data..."
    pool = Pool(processes=num_clients)
    pool.map(run_job, combo)
