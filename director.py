if __name__ == '__main__':
    ## Import builtins
    import sys

    ## Import distsys
    import distsys

    ## Select action
    action = sys.argv[1]

    ## Select additional arguments, if present
    args = []
    if len(sys.argv) > 2:
        args = sys.argv[2:]
        
    distsys.remote_control(action, args)


