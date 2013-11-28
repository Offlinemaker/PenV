import time
import dhtreader
import os
import RPi.GPIO as GPIO		#IO Libraries (kann als GPIO weiter angesprochen werden)
import socket
GPIO.setmode(GPIO.BOARD)	#Setzt den Modus der Pin ansprache auf Board (Numerierungsreinfolge)

GPIO.setup(12, GPIO.IN)	#Setzten von Ports als INPUT
GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

type=11
pin=17

tempfilo="/ramtmp/temp.penv"
humfilo="/ramtmp/hum.penv"
lightfilo="/ramtmp/light.penv"
wetfilo="/ramtmp/wet.penv"
ipfilo="/ramtmp/ip.penv"
doorfilo="/ramtmp/door.penv"

dhtreader.init()
n=0
dc=0
while True:
	if dc>10: dc=0
	if dc%5==0:
		tsuccess=False
		try:
			ot = dhtreader.read(type,pin)
			temp=str(ot[0])
			hum=str(ot[1])
			tsuccess=True
			n=0
		except TypeError:
			tsuccess=False
			n=n+1
		if tsuccess:
			tempIO=os.open(tempfilo, os.O_WRONLY | os.O_CREAT)
			humIO=os.open(humfilo, os.O_WRONLY | os.O_CREAT)
			os.write(tempIO,temp)
			os.write(humIO,hum)
			os.close(tempIO)
			os.close(humIO)
			time.sleep(5)
		else:
			if n>=10:
				tempIO=os.open(tempfilo, os.O_WRONLY | os.O_CREAT)
				humIO=os.open(humfilo, os.O_WRONLY | os.O_CREAT)
				lightIO=os.open(lightfilo, os.O_WRONLY | os.O_CREAT)
				wetIO=os.open(wetfilo, os.O_WRONLY | os.O_CREAT)
				os.write(tempIO,"EE")
				os.write(humIO,"EE")
				os.close(tempIO)
				os.close(humIO)
	if dc%10==0:
		try:	
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(("8.8.8.8",80))
			ip = s.getsockname()[0]
			s.close
		except:
			ip="unresolved"
		try:
			ipIO=os.open(ipfilo, os.O_WRONLY | os.O_CREAT)
			os.write(ipIO, ip)
			os.close(ipIO)
		except:
			fileER=1
	if dc%1==0:
		try:
			ilight=GPIO.input(12)
			iwet=GPIO.input(15)
			idoor=GPIO.input(18)			
			iosuccess=True
		except:
			iosuccess=False
		if iosuccess:
			if ilight==0:
				light="0"
			else:
				light="1"
			if iwet==0:
				wet="1"
			else:
				wet="0"
			if idoor==0:
				door="0"
			else:
				door="1"
			lightIO=os.open(lightfilo, os.O_WRONLY | os.O_CREAT)
			wetIO=os.open(wetfilo, os.O_WRONLY | os.O_CREAT)
			doorIO=os.open(doorfilo, os.O_WRONLY | os.O_CREAT)			
			os.write(lightIO,light)
			os.write(wetIO,wet)
			os.write(doorIO,door)
			os.close(lightIO)
			os.close(wetIO)
			os.close(doorIO)
	time.sleep(1)
		
