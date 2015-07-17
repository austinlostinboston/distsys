# Distsys.messages
## Import builtins
import resource

def reader(msg, host, port):
    address = str(host) + ":" + str(port)
    if msg == 'ping':
        print "Received ping from server, sending echo..."
        rtn_msg = "Echo sent from " + address
    elif msg == "shutdown":
        rtn_msg = "Client " + address + " shutting down."
    elif msg == "mem_stat"
        rtn_msg = "Client " + address + "\n" \
        + "Service Memory Usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024*1024.00)) + "MB" + "\n" \
        + "Child Process Memory Usage: " + str(resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / (1024*1024.00)) + "MB" + "\n"
    else:
        rtn_msg = "Command not understood by clients."
    return rtn_msg