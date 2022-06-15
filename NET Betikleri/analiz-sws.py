#!/usr/bin/python

import os
from urllib.request import HTTPPasswordMgr
from netmiko import (
    ConnectHandler,
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)
from netmiko.hp import HPProcurveSSH, HPProcurveTelnet, HPComwareSSH, HPComwareTelnet


anzswbir = {
    "device_type": "cisco_ios",
    "session_log": "anzswbir_session.log",
    "host": "172.16.10.14",
    "username": "erol.kahraman",
    "password": "=2su18eR",
    "secret": "cisco"
}

anzswiki = {
    "device_type": "cisco_ios",
    "session_log": "anzswiki_session.log",
    "host": "172.16.10.15",
    "username": "erol.kahraman",
    "password": "=2su18eR",
    "secret": "cisco"
}

anzswuc = {
    "device_type": "cisco_ios",
    "session_log": "anzswuc_session.log",
    "host": "172.16.10.16",
    "username": "erol.kahraman",
    "password": "=2su18eR",
    "secret": "cisco"
}

cisco = {
    "device_type": "cisco_ios",
    "host": "172.16.10.1",
    "username": "rtuk-skaas",
    "password": "Mcast.Skaas!Core1",
    "secret": "cisco"
}

hpsw = {
    "device_type": "hp_procurve",
    "host": "172.16.1.5",
    "username": "destek",
    "password": "123qwe",
    # "secret": "cisco"
}



sws = ["anzswbir","anzswiki","anzswuc"]

for sw in sws:
    net_connect = ConnectHandler(**hpsw)
    net_connect.enable()
    output = net_connect.send_command('sh vlan')
    # print(">>>>>>>>>>>>>>>>>> {} <<<<<<<<<<<<<<<<<<".format(sw["host"]))
    print(output)
