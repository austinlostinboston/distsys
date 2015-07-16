'''

'''

# Import builtins
import socket
import sys
import thread
import fcntl
import struct
import os
import multiprocessing

## Import distsys
from messages import reader

class services(object):

    def __init__(self, localhost=False):
        # must call this before anything else
        multiprocessing.Pool.__init__(self)

        self.errors = []
        self.localhost = localhost
        if localhost:
            self.hostIP = '127.0.0.1'
        else:
            self.hostIP = self._getHostIP('eth0')
        self.clients = self._getClients()
        
        
    def _getHostIP(self, card):
        '''
        Returns IP address for the specified network card (eth0, eth1, lo).
        '''
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            hostIP = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', card[:15]))[20:24])
        except:
            error_msg =  "[INIT_ERROR] Could not locate network card " + str(card) + ". Using 127.0.0.1 as default IP."
            print error_msg
            self.errors.append(error_msg)
            hostIP = '127.0.0.1'

        return str(hostIP)


    def _getClients(self):
        '''
        Returns a list of clients listed in the dist.conf or port.conf file.
        This will be used to guide the server when initializing
        connections.

        Ignores lines starting with '#'
        '''
        ## Get's current working directory and removes actions from the path
        file_dir = os.path.dirname(os.path.abspath(__file__)).replace('actions','')
        
        try:
            ## Check to see if system is localized or not
            if self.localhost:
                content = open(file_dir + '/config/port.conf','r')
            else:
                content = open(file_dir + '/config/dist.conf','r')

            lines = content.read().split('\n')
            clients = []

            ## Skips commented lines starting with #
            for line in lines:
                if '#' == line[0]:
                    pass
                else:
                    clients.append(line)

            return clients
        except:
            error_msg = "[INIT_ERROR] Problem reading configuration file"
            print error_msg
            self.errors.append(error_msg)


    def server(self, port, send_msg='', connection_setting='sync'):
        ## Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # ports = [self.port, 15001]
        if connection_setting == 'sync':
            print "Establishing syncronous TCP connections with client..."

            try:
                address = (self.hostIP, port)
                sock.connect(address)
                
                # Sends message if one is present
                if len('send_msg') > 0:
                    sock.sendall(send_msg)
                rec_msg = sock.recv(1024)
                print rec_msg
            finally:
                sock.close()

        if connection_setting == 'async':
            print 'Establishing asyncronous TCP connections with clients...'


    def client(self,port):
        ## Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ## Bind the socket to the host IP address (only one connection per socket allowed)
        address = (self.hostIP, int(port))
        sock.bind(address)

        sock.listen(1)

        print "Service started @ " + str(self.hostIP) + ":" + str(port)

        while True:
            connection, server_address = sock.accept()
            
            try:
                rec_msg = connection.recv(1024)
                msg = reader(rec_msg, self.hostIP, port)
                connection.sendall(msg)
            finally:
                print "closing connection with server."
                connection.close()
                if rec_msg == 'shutdown':
                    print "Client " + self.hostIP + ":" + port + " stopped..."
                    break

# s = services(localhost=True)
# print s.clients
# print async.poop()
