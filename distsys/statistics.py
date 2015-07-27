#!/usr/bin/python
import os
import subprocess
import re
import math

class clientStatus(object):
    info = os.statvfs("/")

    def __init__(self):
        self.size = self._size('GB')
        self.free_mem = self._memFree()
        self.total_mem = self._memTotal()

        self.free_disk = self._diskFree()
        self.total_disk = self._diskTotal()

    def _memFree(self):
        return None

    def _memTotal(self):
        return None

    def _diskFree(self):
        hd_free = "%.2f" % ((self.info.f_bavail * self.info.f_frsize) / self.size)
        return hd_free

    def _diskTotal(self):
        hd_total = "%.2f" % ((self.info.f_blocks * self.info.f_frsize) / self.size)
        return hd_total

    def _size(self, size):
        power = 0

        if size == 'KB':
            power = 1
        elif size == 'MB':
            power = 2
        elif size == 'GB':
            power = 3
        elif size == 'TB':
            power = 4
        else:
            pass

        return math.pow(1024,power)

def online(ip_addr, packets=2):
    ## Use unix 'ping' comand and parse output
    ping = subprocess.check_output(["ping", "-c", str(packets), str(ip_addr)],stderr=subprocess.STDOUT)
    packets_received = ping.split("\n\n")[1].split("\n")[1].split(", ")[1]

    n_packets = int(re.findall('\d+', packets_received)[0])
    if n_packets == packets:
        return True
    else:
        return False

def mkdir(ip_addr, path, directory):
    #mkdir = subprocess.call(["ssh", "-T", str(ip_addr), "\'", "cd", path, ";", "mkdir", directory,"\'"],stderr=subprocess.STDOUT)
    ssh = 'ssh -T ' + str(ip_addr) + ' '
    cd = 'cd ' + path +'; '
    mkdir = 'mkdir ' + directory
    os.system(ssh + "\'" + cd + mkdir + "\'")
    print ip_addr + ":\tcreated \033[94m" + path + "/" + directory + "\033[0m"
