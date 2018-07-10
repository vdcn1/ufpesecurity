import sys
import os
import commands
import csv
import time
import signal
import subprocess

#os.system("iw phy phy0 interface add mon0 type monitor")
#os.system("ifconfig mon0 up")
#os.system("airodump-ng mon0 -w out")
#os.kill(os.getppid(),signal.SIGHUP)

process = subprocess.Popen(['iw','phy','phy0','interface','add','mon0','type','monitor'])
process1 = subprocess.Popen(['ifconfig','mon0','up'])
process2 = subprocess.Popen(['airodump-ng','mon0','-w','out'])
#time.sleep(5)

tag = 0
i = -2
argumento = "Station MAC  First time seen  Last time seen  Power  # packets  BSSID  Probed ESSIDs"

with open('out.txt', "w") as my_output_file:
    with open('out-01.csv', "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()


out = open('out.txt', 'r')
texto = out.readlines()
process2.kill()
process1.kill()
process.kill()
for linha in texto :
    if argumento == linha.strip():
	tag = 1
    if tag == 1:
	i = i + 1

print "Quantidade de pessoas na parada eh:" + str(i)
out.close()
os.system("rm out*.*")
out = open('out.txt', 'r+')
out.write(i)
print str(i)
out.close()
sys.exit()
    	#os.system("python brainwallet-check.py '" + argumento + "'")
