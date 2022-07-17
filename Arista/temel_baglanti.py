#!/usr/bin/python

from cgitb import text
from jsonrpclib import Server
# import ssl

# ssl._https_verify_certificates( False )

switch = Server( "http://admin:arista@10.10.1.8/command-api" )
response = switch.runCmds( 1, [ "show version" ], "text")

print(response[0]["output"])

# print ('Switch MAC address is: ' , response[0] [ "systemMacAddress" ])
# print ('Switch Vesrion is ' , response[0] [ "version" ])
# print ('Switch Mode Name is ' , response[0] [ "modelName" ])