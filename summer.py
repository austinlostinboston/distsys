#!/usr/bin/python

data_dir = "~/distsys/data/sum_test"
output_dir = "~/distsys/output/sum_test/"

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
        count += int(line)
    r.close()

w = open(output_dir + "output_1.txt")
w.write(count)
w.close()