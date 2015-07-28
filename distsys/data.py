## Import builtins
import os
import random

def mkdir(ip_addr, path, directory):
    '''
    Makes a directory at ip_addr:/path/directory
    '''
    ssh = 'ssh -T ' + str(ip_addr) + ' '
    cd = 'cd ' + path +'; '
    mkdir = 'mkdir ' + directory
    os.system(ssh + "\'" + cd + mkdir + "\'")
    print "created \033[94m" + path + "/" + directory + "\033[0m" + " @" + ip_addr

def distribute_data(num_clients, path):
    ## Gat all files in dir
    files = getAllFiles(path)
    print "Found " + str(len(files)) + "at " + path

    ## Split up files randomly among clients
    client_files = splitFiles(files, num_clients)

    return client_files

def getAllFiles(path):
    '''
    Collects paths for all files within path
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        if len(filenames) > 0:
            for f in filenames:
                file_path = dirpath + "/" + f
                files.append(file_path)

    return files

def splitFiles(files, num_clients):
    '''
    Splits a list of files up randomly into N_client groupings
    '''
    clients = range(num_clients)
    client_files = [[] for _ in clients]

    for f in files:
        rnd_client = random.choice(clients)
        print "File " + f + " stored on client " + str(rnd_client)
        cf = client_files[rnd_client]
        cf.append(f)

    return client_files

# files = getAllFiles(".")
# print "Files: " + str(len(files))
# cf = splitFiles(files, 20)
# print cf