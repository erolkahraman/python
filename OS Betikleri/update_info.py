#!/usr/bin/python
# coding=utf-8
import os
import time
import pxssh
import getpass

HFILE = "/opt/skaas/scripts/update_files/config/hosts"

with open (HFILE,"r") as F:
  hosts = F.readlines()
  for host in hosts:
      username = "sadmin"
      password = "Sadm1234"
      try:
        s = pxssh.pxssh()
        s.login (host.strip(), username, password)
        s.sendline ('echo Sadm1234| sudo -S echo -e "\n================================\n10.1.1.22       ebystest.rtuk.gov.tr\n10.10.110.11    ebys.rtuk.gov.tr\n================================\n" | sudo -S tee -a /etc/hosts')
        s.sendline ('echo Sadm1234| sudo -S echo -e "\n================================\n10.1.1.22       ebystest.rtuk.gov.tr\n10.10.110.11    ebys.rtuk.gov.tr\n================================\n" | sudo -S tee -a /etc/hosts')
        s.prompt()
        print("{} güncellendi. ".format (host.strip()))
        s.logout()
      except pxssh.ExceptionPxssh, e:
        print ("{} guncellenemedi!".format(host.strip()))
        print ("HATA:",str(e))
F.close()
