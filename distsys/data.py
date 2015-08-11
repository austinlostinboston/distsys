## Import builtins
import os
import random
import subprocess
import pipes
from distsys.config.settings import __serverHomeDir__ , __clientHomeDir__

## Import distsys
from distsys.utils import emptyList, extractNum

def mkdir(ip_addr, path, directory):
    '''
    Makes a directory at ip_addr:/path/directory
    '''
    ssh = 'ssh -T ' + str(ip_addr) + ' '
    cd = 'cd ' + path +'; '
    mkdir = 'mkdir ' + directory
    if remote_path_exists(ip_addr, path):
        print "Directory " + directory + " already exists at " + ip_addr 
    else:
        os.system(ssh + "\'" + cd + mkdir + "\'")
        print "created \033[94m" + path  + directory + "\033[0m" + " @" + ip_addr

def remote_path_exists(ip_addr, path):
    '''
    Checks whether a file or dir exists on a specific client
        ip_addr: the ip address in which you are checking for the file/dir
        path: The path of the file or dir that is being checked
    '''

    ## Replace ~ (home symbol) with specific path
    if '~' in path:
        path = path.replace('~',__serverHomeDir__ + path)

    print "checking path: " + path

    ## Check path
    resp = subprocess.call(['ssh', ip_addr, 'test -e %s' % pipes.quote(path)])
    if resp == 0:
        return True
    else:
        return False
    
def run_script(ip_addr, path):
	os.system("ssh %s \'python %s\'" % (ip_addr, path))

def distribute_data(num_clients, path, job=False):
    '''
    Distributes all files found under 'path' and distributes them to the number of clients specified
        num_clients: The number of clients files will be distributed to.
        path: absolute path where data files can be found
        job: if the file is a script/job


        returns: the output from file distributing method
    '''
    if job:
        client_files = [[path]] * num_clients
    else:
        ##Get all files in dir
        files = getAllFiles(path)
        total_files = len(files)
        print "Found " + str(len(files)) + " files in " + path

        ## Split up files randomly among clients
        #client_files = splitFilesRandom(files, num_clients)
        client_files = splitFilesMod(files, num_clients)

    return client_files, total_files

def collect_results(ip_addr, project_name):
    remote_path = "~/distsys/output/" + project_name + "/*"
    local_path = "~/austin/distsys/output/" + project_name
    os.system('scp ' + ip_addr + ":" + remote_path + " " + local_path)

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
    valid_ext = ['txt','json','zip','gz']

    for f in files:
        file_name = f.split("/")[-1]
        file_ext = f.split(".")[-1]

        ## Only distribute data files
        if file_ext in valid_ext:
            num = extractNum(file_name)

            ## Subtract 1 from the number before mod so file 1.txt goes to client 1 rather than client 2.
            mod_client = (num - 1) % num_clients
            cf = client_files[mod_client]
            cf.append(f)

    return client_files

# files = getAllFiles(".")
# print "Files: " + str(len(files))
# cf = splitFiles(files, 20)
# print cf
