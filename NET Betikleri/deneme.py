from asyncio.subprocess import DEVNULL, PIPE
from multiprocessing.spawn import import_main_path
import os
import subprocess as sp
from unittest import result

result = os.system("ping -c 1 localhost > /dev/null")
ping1 = sp.Popen(["ping","-c 1","localhost1"],stdout=sp.PIPE,stderr=PIPE,text=True)


(out,err)=ping1.communicate()

# print (ping)
# print (out)

# if ping1.returncode == 0:
#     print(out)
#     print("Host is UP")
# else:
#     print(err)
#     print("Host is DOWN")


if result == 0:
    print("Host is UP")
    print(result)
else:
    print("Host is DOWN")
    #print(result)