import sys
import os
import commands
import csv
import time
import signal
import subprocess

tag = 0
i = -2
argumento = "Station MAC  First time seen  Last time seen  Power  # packets  BSSID  Probed ESSIDs"

with open('out.txt', "w") as my_output_file:
    with open('out-01.csv', "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()


out = open('out.txt', 'r')
texto = out.readlines()

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

