#!/usr/bin/python

## Import builtins
import sys
from multiprocessing import Process, Pool

## Import distsys
from distsys.services import services

## Startup service
local_service = services(localhost=True)
num_clients = len(local_service.clients)

msg = "mem_stat"
for client in local_service.clients:
    local_service.server(int(client), send_msg=msg)