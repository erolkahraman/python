#!/usr/bin/python

from jsonrpclib import Server
import ssl

ssl._https_verify_certificates( False )

switch = Server( "https://admin:arista@10.10.1.8/command-api" )
response = switch.runCmds( 1, [ "show version" ] )
print ('Switch MAC address is: ' , response[0] [ "systemMacAddress" ])
print ('Switch Vesrion is ' , response[0] [ "version" ])
print ('Switch Mode Name is ' , response[0] [ "modelName" ])