# Distsys.utils - a submodule containing miscellaneou methods not belonging to other modules.

## Import builtins
import re
import hashlib

def emptyList(length):
    ## Creates a list of empty lists where each empty list independent of one another.
    main_list = range(length)
    empty_list = [[] for _ in main_list]

    return empty_list

def extractNum(string):
    nums = re.findall(r'\_(\d+)\.', string)[-1]
    return int(nums)
