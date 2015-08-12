import sys
import subprocess

resp = subprocess.check_output(['ssh', '192.168.1.1', 'md5sum', '/home/jpfeffer/distsys/data/test/1.txt'])

print resp.split(' ')[0]
