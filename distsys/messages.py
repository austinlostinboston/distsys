# Distsys.messages
## Import builtins
import resource
import os

## import distsys
from distsys.statistics import clientStatus

def reader(msg, host, port):
    address = str(host) + ":" + str(port)
    if msg == 'ping':
        print "Received ping from server, sending echo..."
        rtn_msg = "Echo sent from " + address

    elif msg == "shutdown":
        rtn_msg = "Client " + address + " shutting down."

    elif msg == "mem_stat":
        print "mem_stat request from server."
        rtn_msg = "Client " + address + "\n" \
        + "Service Memory Usage: " + str("%.4f" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024*1024.00))) + " MB" + "\n" \
        + "Child Process Memory Usage: " + str("%.4f" % (resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / (1024*1024.00))) + " MB" + "\n"
    elif msg == "stat":
        print "stat request from server."
        cs = clientStatus()
        hd_free = cs.free_disk
        hd_total = cs.total_disk
        hd_percent = "%.2f\%" % (hd_free / hd_total)
    else:
        rtn_msg = "Command not understood by clients."
    return rtn_msg