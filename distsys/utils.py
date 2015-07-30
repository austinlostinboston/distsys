# Distsys.utils - a submodule containing miscellaneou methods not belonging to other modules.

## Import builtins
import re

def emptyList(length):
    ## Creates a list of empty lists where each empty list independent of one another.
    main_list = range(length)
    empty_list = [[] for _ in clients]

    return empty_list

def extractNum(string):
    num = int(re.search(r'\d+', string).group())
    return num
