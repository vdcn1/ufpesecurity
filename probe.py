import os
import commands

os.system("iw ohy ohy0 interface add mon0 type monitor")
os.system("ifconfig mon0 up")
os.system("airodump-ng mon0 -w out")

#Pausar aqui Manualmente
