#!/usr/bin/python3

from asyncio.subprocess import DEVNULL
import subprocess as sp
from subprocess import PIPE
from sys import stderr
from unittest.result import STDERR_LINE
from netmiko import ConnectHandler as CH
import time

class Whiptail:

    def __init__(self):
        pass

    def w_input(self,metin="AÇIKLAMA",baslik="BAŞLIK",en=0,boy=0):
        command = 'whiptail --inputbox "{}" --title "{}" {} {}'.format(metin,baslik,boy,en)
        result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
        out,err = result.communicate()
        return err

    def w_msg(self,metin="MESAJ",baslik="BAŞLIK",en=0,boy=0):
        command = 'whiptail --scrolltext --msgbox "{}" --title "{}" {} {}'.format(metin,baslik,boy,en)
        result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
        out,err = result.communicate()
        return err

    def w_onay(self,metin="MESAJ",baslik="BAŞLIK",en=0,boy=0):
        command = 'whiptail --yesno "{}" --title "{}" {} {}'.format(metin,baslik,boy,en)
        result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
        out,err = result.communicate()
        return err


WhipT1 = Whiptail()

# mesajj = WhipT1.w_input().decode("utf-8")
# print (WhipT1.w_msg(metin=mesajj).decode("utf-8"))

print(WhipT1.w_onay())