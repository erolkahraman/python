#!/usr/bin/python3

from asyncio.subprocess import DEVNULL
import subprocess as sp
from subprocess import PIPE
from sys import stderr
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
        #command = 'whiptail --yesno "{}" --title "{}" {} {}'.format(metin,baslik,boy,en)
        command = f'whiptail --yesno "{metin}" --title "{baslik}" {boy} {en}'
        result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
        out,err = result.communicate()
        return result.returncode
    
    def w_menu(self,metin="MENU",baslik="BAŞLIK",liste=[],en=0,boy=0):
        """
        ======== BASLIK =======
        MENU
        1 Secenek1
        2 Secenek2
        3 Secenek3
        =======================
        NOT: 
        - Menu tag degerleri 1 den baslayarak artmaktadir.
        - Tag degerleri gizlenmektedir (--notags).
        """    

        i = 1
        secenek = []
        for menu_elemani in liste:
            secenek.append(str(i))
            secenek.append(menu_elemani)
            i += 1
        print ("=================\n",secenek)
        command = 'whiptail --menu "{}" --notags --title "{}" {} {} {} {}'.format(metin,baslik,boy,en,len(liste),' '.join(secenek))
        result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
        out,err = result.communicate()
        return int(err.decode("utf-8")),result.returncode


WhipT1 = Whiptail()

# mesajj = WhipT1.w_input().decode("utf-8")
# print (WhipT1.w_msg(metin=mesajj).decode("utf-8"))


print(WhipT1.w_menu(en=30,boy=10,liste=["bir","iki","üç","dört"]))