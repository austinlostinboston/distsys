import os
import subprocess
import re

#os.system("ping 127.0.0.1 -c 2")
ip_addr = "127.0.0.1"
p = subprocess.check_output(["ping", "-c", "2", ip_addr],stderr=subprocess.STDOUT)

