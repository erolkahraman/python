import os
import subprocess
import time
from unittest import result

class Net():
    def __init__(self,host):
        self.host = host
    def ping (self):
        result = os.system("ping -c 1 " + self.host + " > /dev/null")
        if  result == 0:
            print ("Host is UP.")
        else:
            print ("Host is DOWN")


def ping1 (host):
    result = os.system("ping -c 1 " + host + " > /dev/null")
    if  result == 0:
        print ("{} is UP.".format(host))
    else:
        print ("{} is DOWN".format(host))
# host1 = Net("localhost")
# host1.ping()

for i in range(1,50):
    ping1("172.16.1." + str(i))