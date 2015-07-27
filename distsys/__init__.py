## Import builtins
from subprocess import call

__version__ = '0.0.1'
__author__ = 'Austin Ankney'
__license__ = None

## Other global things

## Handles running services from the command line. Inspired by django <3 <3 <3
def remote_control(action, arguments):
    try:
        exec_path = './distsys/actions/' + action + '.py'
        command = ['python', exec_path]

        if len(arguments) > 0:
            command.extend(arguments)
            
        call(command)

    except:
        error_msg = '[RUN_ERROR] Action could not be executed. Check spelling.'
        print error_msg