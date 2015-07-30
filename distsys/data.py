## Import builtins
import os
import random

## Import distsys
from distsys.utils import emptyList, extractNum

def mkdir(ip_addr, path, directory):
    '''
    Makes a directory at ip_addr:/path/directory
    '''
    ssh = 'ssh -T ' + str(ip_addr) + ' '
    cd = 'cd ' + path +'; '
    mkdir = 'mkdir ' + directory
    os.system(ssh + "\'" + cd + mkdir + "\'")
    print "created \033[94m" + path + "/" + directory + "\033[0m" + " @" + ip_addr

def remoteDirExists(ip_addr, path):
    pass

def distribute_data(num_clients, path):
    '''
    Distributes all files found under 'path' and distributes them to the number of clients specified
        num_clients: The number of clients files will be distributed to.
        path: absolute path where data files can be found

        returns: the output from file distributing method
    '''
    ## Gat all files in dir
    files = getAllFiles(path)
    print "Found " + str(len(files)) + "at " + path

    ## Split up files randomly among clients
    #client_files = splitFilesRandom(files, num_clients)
    client_files = splitFilesMod(files, num_clients)

    return client_files

def getAllFiles(path):
    '''
    Collects the absolute path for each file found under 'path'
    path: absolute path to be searched for files

        returns: a list containing absolute paths for all files found under 'path'
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(path):
        if len(filenames) > 0:
            for f in filenames:
                file_path = dirpath + "/" + f
                files.append(file_path)

    return files

def splitFilesRandom(files, num_clients):
    '''
    This data distribution method random assigns which file from files is sent to each client.

    files: a list of absolute file paths
    num_clients: the number of clients to be distributed to.

        returns: a list with num_clients lists in it. Each sublist corresponds to a client and
            contains the path of the data file that will be distributed to that client. 
    '''
    client_files = emptyList(num_clients)

    for f in files:
        rnd_client = random.choice(clients)
        print "File " + f + " stored on client " + str(rnd_client)
        cf = client_files[rnd_client]
        cf.append(f)

    return client_files

def splitFilesMod(files, num_clients):
    '''
    This data distribution method assigns recipients based a value within the file name.
        this value is then modded by num_clients whos result is used to determine the recipient of the file.

    files: a list of absolute file paths
    num_clients: the number of clients to be distributed to.

    returns: a list with num_clients lists in it. Each sublist corresponds to a client and
            contains the path of the data file that will be distributed to that client. 
    '''
    client_files = emptyList(num_clients)

    for f in files:
        file_name = f.split("/")[-1]
        num = extractNum(file_name)
        mod_client = num % num_clients
        cf = client_files[mod_client]
        cf.append(f)

    return client_files

# files = getAllFiles(".")
# print "Files: " + str(len(files))
# cf = splitFiles(files, 20)
# print cf