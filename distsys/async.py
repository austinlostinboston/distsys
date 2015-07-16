# distsys.async
# A helper module for setting up asyncronous connections between clients and a server.
import services

def poop():
    return "poop"

s = services.services(localhost=True)
print s.hostIP
print s.clients