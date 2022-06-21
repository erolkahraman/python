#!/usr/bin/python



from cisco_access import c_omurga,c_commands
from netmiko import ConnectHandler

print(c_omurga())
cmd1 = c_commands("sh_ver")
net_connect = ConnectHandler(**c_omurga())
net_connect.enable()
output = net_connect.send_command(cmd1)

print(output)