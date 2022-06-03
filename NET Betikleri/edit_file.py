#!/usr/bin/python

import os
from pexpect import pxssh
import getpass


HOST_FL = "/tmp/hosts"


s = pxssh.pxssh()
if not s.login ('localhost', 'destek', '123qwe'):
    print ("SSH session failed on login.")
    print (str(s))
else:
    print ("SSH session login successful")
    s.sendline ('printf "1.1.1.1 abc\n2.2.2.2 xyz" >> /tmp/hosts')
    s.prompt()         # match the prompt
    print (s.before)     # print everything before the prompt.
    s.logout()



with open (HOST_FL,"a") as fl:
    deneme = """1.1.1.1 host1
    2.2.2.2 host2
    3.3.3.3 host3
    """
    fl.write(deneme)
fl.close()