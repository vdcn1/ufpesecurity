import serial
import pyrebase
import time

config = {
  "apiKey": "AIzaSyDyo9fIt9g0bjkezqhKILASPdxndao5200",
  "authDomain": "ufpesecurity-c3d0e.firebaseapp.com",
  "databaseURL": "https://ufpesecurity-c3d0e.firebaseio.com",
  "storageBucket": "ufpesecurity-c3d0e.appspot.com"
} #firebase configuration

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database() #authenticating and geting database reference

ser = serial.Serial('/dev/ttyUSB0',9600) #on the rasp, setting up serial communication
s = [0,1]
while True:
	luminosity = ser.readline() #reading luminosity intensity from serial
	s[0] = str(ser.readline()) #string garbage
	print (s[0])
	time.sleep(1) #small delay for not overworking firebase
	luminosity = luminosity[:-2] #ticking out garbage
	db.child("Local 1").update({"Luminosidade": luminosity})
	print (luminosity) #debugging purposes
