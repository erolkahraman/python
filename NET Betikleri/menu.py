#!/usr/bin/python3

from asyncio.subprocess import DEVNULL
import subprocess as sp
from subprocess import PIPE
from sys import stderr
from unittest.result import STDERR_LINE
from netmiko import ConnectHandler as CH
import time

s_omurga = {
    "device_type": "cisco_ios",
    "host": "172.16.10.1",
    "username": "rtuk-skaas",
    "password": "Mcast.Skaas!Core1",
    "secret": "cisco"
}

conn_omurga = CH(**s_omurga)
conn_omurga.enable()

c_show_ver = "show version"
c_show_vlan = "show vlan"

# c_create_lo = [
#     "configure terminal",
#     "interface lo 3",
#     "description HOHOHO"
# ]
# output = conn_omurga.send_command(c_show_vlan)
# output = conn_omurga.send_config_set(c_create_lo)
# print(output)

# conn_omurga.disconnect()

# result = sp.Popen("whiptail --msgbox --title DENEME 'Bu bir denemedir...' 10 40",stdout=stderr,stderr=PIPE,shell=True)
#result = sp.Popen('whiptail --menu "" --notags --title "Net Komutları" 10 40 3 "1" "sh ver" "2" "sh users"',stdout=stderr,stderr=PIPE,shell=True)
# result = sp.Popen('whiptail --inputbox "DENEME" --title "BASLIK" 10 30',stdout=stderr,stderr=PIPE,shell=True)

# out,err = result.communicate()

# print(err)

def w_input(metin="AÇIKLAMA",baslik="BAŞLIK",en=40,boy=10):
    command = 'whiptail --inputbox "{}" --title "{}" {} {}'.format(metin,baslik,boy,en)
    result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
    out,err = result.communicate()
    return err

def w_msg(metin="MESAJ",baslik="BAŞLIK",en=100,boy=20):
    command = 'whiptail --scrolltext --msgbox "{}" --title "{}" {} {}'.format(metin,baslik,boy,en)
    result = sp.Popen(command,stdout=stderr,stderr=PIPE,shell=True)
    out,err = result.communicate()
    return err

c_create_lo = [
    "interface lo 3"
]

IP_ADDRES = w_input(metin="Interface IP address",baslik="IP ADDRESS")
IP_MASK = w_input(metin="IP mask (255.255.255.0)",baslik="IP MASK")
INT_DESC = w_input(metin="Interface Description",baslik="DESCRIPTION")

c_create_lo.append("description " + INT_DESC.decode("utf-8"))
c_create_lo.append("ip address " + IP_ADDRES.decode("utf-8") + " " + IP_MASK.decode("utf-8"))
output = conn_omurga.send_config_set(c_create_lo)
print (w_msg(metin=output,en=100,boy=20).decode("utf-8"))


# if (int(err.decode("utf-8")) == 1):
#     print ("show version komutu seçildi")
#     print("#"*40)
#     time.sleep(2)
#     output = conn_omurga.send_command(c_show_ver)
#     print (w_msg(metin=output,en=100,boy=20).decode("utf-8"))
#     conn_omurga.disconnect()
# elif (int(err.decode("utf-8")) == 2):
#     print ("show vlan komutu seçildi")
#     output = conn_omurga.send_command(c_show_vlan)
#     print (output)
#     conn_omurga.disconnect()
# else:
#     print("Bir seçim yapılmadı")

# print (w_msg().decode("utf-8"))