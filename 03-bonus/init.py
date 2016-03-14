import lldb

def init(debugger, command, result, internal_dict):
    debugger.HandleCommand('breakpoint set -name main')
    debugger.HandleCommand('run')
    debugger.HandleCommand('script print "\033[32mThread STARTED and Waiting\033[0m"')


def __lldb_init_module(debugger, dict):
    debugger.HandleCommand('script print "\033[32m[INIT COMMAND IMPORT]\033[0m"')
    debugger.HandleCommand('command script add -f init.init init -h "init puts a breakpoint on main and run the process"')
