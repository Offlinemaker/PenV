import time
import serial
import os
from time import gmtime, strftime

comm = "\x9F"
poff = "\x82"
pon  = "\x83"
initack = "\xA5"
chead= "\xFE"
cls = "\x65"
cursor= "\xFF"
doorfilo="/ramtmp/door.penv"
tempfilo="/ramtmp/temp.penv"
humfilo="/ramtmp/hum.penv"
lightfilo="/ramtmp/light.penv"
wetfilo="/ramtmp/wet.penv"
ipfilo="/ramtmp/ip.penv"

st=0.05 #Sleep Time
screen = serial.Serial(port='/dev/ttyAMA0',parity='N', baudrate=9600, timeout=0, stopbits=1, bytesize=8)
def init_screen():
	#screen.open()
	screen.write(comm)
	time.sleep(st)
	screen.write(poff)
	time.sleep(st)
	screen.write(comm)
	time.sleep(st)
	screen.write(pon)
	time.sleep(st)
	screen.write(initack)

def rone(string):
	screen.write(comm)
        time.sleep(st)
        screen.write(cursor)
        time.sleep(st)
        screen.write("00")
	time.sleep(st)
	screen.write(comm)
	time.sleep(st)
	screen.write(chead)
	time.sleep(st)
	screen.write(string)

def rtwo(string):
	screen.write(comm)
        time.sleep(st)
        screen.write(cursor)
        time.sleep(st)
        screen.write("01")
	time.sleep(st)
	screen.write(comm)
	time.sleep(st)
	screen.write(chead)
	time.sleep(st)
	screen.write(string)

def clear():
	screen.write(comm)
	time.sleep(st)
	screen.write(cls)
	time.sleep(st)

init_screen()
screen.close()
n=0
s=0
screen.open()
while True:
	#screen.open()
	if screen.read()=='c':
        	rone("Maintenance-MODE")
		rtwo("Start [y/n]     ")
		mm=0
		while mm<60:
			if screen.read()=='y':
				rtwo("OK! Started     ")
				screen.write(comm)
				screen.close()
				os.system("/sbin/getty -L ttyAMA0 9600 vt100")
				exit()
			elif screen.read()=='n':
				break
			else:
				mm=mm+1
				time.sleep(1)
	n=n+1
	if n>=120 or s==0 or s==15 or s>= 30:
		clear()
		if n>=120: n=0
		if s==30: s=0
	if s<15:
		try:
			lightIO=os.open(lightfilo, os.O_RDONLY | os.O_NONBLOCK)
			wetIO=os.open(wetfilo, os.O_RDONLY | os.O_NONBLOCK)
			doorIO=os.open(doorfilo, os.O_RDONLY | os.O_NONBLOCK)
			light=os.read(lightIO,1024)
			wet=os.read(wetIO,1024)
			door=os.read(doorIO,1024)
			os.close(lightIO)
			os.close(wetIO)
			os.close(doorIO)
		except:
			light="xE"
			wet="xE"
			door="xE"
		if (n%5)==1:
			try:
				tempIO=os.open(tempfilo, os.O_RDONLY | os.O_NONBLOCK)
				humIO=os.open(humfilo, os.O_RDONLY | os.O_NONBLOCK)
				temp=os.read(tempIO,1024)
				hum=os.read(humIO,1024)
				os.close(tempIO)
				os.close(humIO)
			except:
				temp="WxxW"
				hum="WxxW"
		rone("L_")
		screen.write(light)
		screen.write(" W_")
		screen.write(wet)
		screen.write(" D_")
		screen.write(door)
		screen.write("     ")
		rtwo("T=")
		screen.write(temp)
		screen.write("C H=")
		screen.write(hum)
		screen.write("%")
	if s>15:	
		rone(strftime("%H:%M:%S     IP:", gmtime()))
		try:
			ipIO=os.open(ipfilo, os.O_RDONLY | os.O_NONBLOCK)
			ip=os.read(ipIO,1024)
			os.close(ipIO)
		except:
			ip="noFile"
		rtwo(ip)
	#strftime("%Y-%m-%d \n %H:%M:%S", gmtime()))
	time.sleep(st)
	s=s+1	
        
		
		#screen.write(comm)
		#time.sleep(st)
		#screen.write(cursor)
        	#time.sleep(st)
		#screen.write("/x0F")
                #time.sleep(st)
                #screen.write(chead)
                #time.sleep(st)
                #screen.write(" ")	
	
	#screen.write(strftime("%Y-%m-%d", gmtime()))

	#screen.close()
	
