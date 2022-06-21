#!/usr/bin/python


import cisco_access
from cisco_access import c_omurga
from netmiko import ConnectHandler

print(c_omurga())
cmd1 = cisco_access.Commands.sh_ver()
net_connect = ConnectHandler(**c_omurga)
net_connect.enable()
output = net_connect.send_command("cmd1")

print(output)