import lldb

def reverse(debugger, command, result, internal_dict):
	if debugger.GetSelectedTarget():
		s = str(debugger.GetSelectedTarget())
		print("FT_" + s[::-1])

def __lldb_init_module(debugger, dict):
	debugger.HandleCommand('command script add -f reverse.reverse reverse')  
