#!/usr/bin/python

from cmath import cos


def c_omurga():
    omurga = {
        "device_type": "cisco_ios",
        "host": "172.16.10.1",
        "username": "rtuk-skaas",
        "password": "Mcast.Skaas!Core1",
        "secret": "cisco"
    }
    return omurga

def c_commands(cmd):
    commands = {
       "sh_ver": "show version"
    }
    return commands[cmd]