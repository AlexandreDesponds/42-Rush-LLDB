import lldb
import os.path

def import_conf(debugger, command, result, internal_dict):
    s = str(debugger.GetSelectedTarget()) + ".config"
    if os.path.isfile(s):
		with open(s) as f:
			for line in f:
				line = str(line).rstrip('\n')
				if not line == "continue":
					debugger.HandleCommand(line)
		return
    if os.path.isfile("commandes"):
		with open("commandes") as f:
			for line in f:
				line = str(line).rstrip('\n')
				if not line == "continue":
					debugger.HandleCommand(line)
		return

def __lldb_init_module(debugger, dict):
    debugger.HandleCommand('script print "\033[32m[IMPORT CONFIG COMMAND IMPORT]\033[0m"')
    debugger.HandleCommand('command script add -f import_conf.import_conf import -h "This command detect a <file>.config file or commandes file and execute its commands');
