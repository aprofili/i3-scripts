#!/usr/bin/python3
from i3ipc import Connection, Event
import sys

i3 = Connection()

workspaces = i3.get_workspaces()
current_ws = [ws for ws in workspaces if ws.focused][0]
ws_on_output = [ws for ws in workspaces if ws.output == current_ws.output]
# print((ws_on_output,current_ws))
if sys.argv[1] == "forward":
    next_num = ws_on_output[(ws_on_output.index(current_ws)+1)%len(ws_on_output)].num
elif sys.argv[1] == "backward":
    next_num = ws_on_output[ws_on_output.index(current_ws)-1].num
else:
    print("Error: No valid direction supplied.")
    next_num = current_ws.num

i3.command('workspace number %d'%next_num)
