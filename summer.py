#!/usr/bin/python
import os
import socket

data_dir = os.path.expanduser("~/distsys/data/sum_test")
output_dir = os.path.expanduser("~/distsys/output/sum_test")
client_name = socket.gethostname()
count = 0

## Extract data file paths
files = []
for dirpath, dirnames, filenames in os.walk(data_dir):
    for f in filenames:
        file_path = dirpath + "/" + f
        files.append(file_path)

## Read each file
for f in files:
    r = open(f,'r')
    content = r.read()
    lines = content.split("\n")

    for line in lines:
	if line != ' ' and len(line) > 0:
        	count += int(line)
    r.close()

w = open(output_dir + "/output_" + client_name + ".txt", 'w')
w.write(str(count))
w.close()
