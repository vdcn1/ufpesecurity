import serial
import pyrebase
import time
import os

config = {
  "apiKey": "AIzaSyDyo9fIt9g0bjkezqhKILASPdxndao5200",
  "authDomain": "ufpesecurity-c3d0e.firebaseapp.com",
  "databaseURL": "https://ufpesecurity-c3d0e.firebaseio.com",
  "storageBucket": "ufpesecurity-c3d0e.appspot.com"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

ser = serial.Serial('/dev/ttyUSB0',9600)
s = [0,1]
#p = subprocess.Popen(['python','CountDevices.py'])

while True:
	read_serial = ser.readline()
	s[0] = str(ser.readline())	
	print (s[0])
	time.sleep(1)
	read_serial = read_serial[:-2]
	#os.system("python CountDevices.py")
	f = open("out.txt","r")
	pop = f.readline()
	db.child("Local 1").update({"Luminosidade": read_serial})
	db.child("Local 1").update({"pop": pop})
	f.close()
	print (read_serial)
