# Distsys.messages

def reader(msg, host, port):
    address = str(host) + ":" + str(port)
    if msg == 'ping':
        print "Received ping from server, sending echo..."
        rtn_msg = "Echo sent from " + address
    elif msg == "shutdown":
        rtn_msg = "Client " + address + " shutting down."
    elif msg[0:2] == "add":
        pass
    else:
        rtn_msg = "Command not understood by clients."
    return rtn_msg