#!/usr/bin/python

from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)


cisco = {
    "device_type": "cisco_ios",
    "host": "172.16.10.1",
    "username": "rtuk-skaas",
    "password": "Mcast.Skaas!Core1",
    "secret": "cisco"
}

net_connect = ConnectHandler(**cisco)
net_connect.enable()

output = net_connect.send_command('show version')

print(output)