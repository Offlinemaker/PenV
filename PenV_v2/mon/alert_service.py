import time
import os
import RPi.GPIO as GPIO
time.sleep(30)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

ring=GPIO.PWM(7,4000)
blink=GPIO.PWM(22,2)

tempfilo="/ramtmp/temp.penv"
humfilo="/ramtmp/hum.penv"
lightfilo="/ramtmp/light.penv"
wetfilo="/ramtmp/wet.penv"
ipfilo="/ramtmp/ip.penv"

wftemp="/mon/vals/wftemp.conf"
cftemp="/mon/vals/cftemp.conf"
wfhum="/mon/vals/wfhum.conf"
cfhum="/mon/vals/cfhum.conf"
cfwet="/mon/vals/cfwet.conf"

silent=0

warning=0
critical=0

warn_blink=0

crit_ring=0
crit_blink=0

ring_act=0
blink_act=0

sc=0
cwsuc=0
while cwsuc==0:
	try:
		wftempIO=os.open(wftemp, os.O_RDONLY | os.O_NONBLOCK)
		tempW=os.read(wftempIO,1024)
		os.close(wftempIO)
		cftempIO=os.open(cftemp, os.O_RDONLY | os.O_NONBLOCK)
		tempC=os.read(cftempIO,1024)
		os.close(cftempIO)
		wfhumIO=os.open(wfhum, os.O_RDONLY | os.O_NONBLOCK)
		humW=os.read(wfhumIO,1024)
		os.close(wfhumIO)
		cfhumIO=os.open(cfhum, os.O_RDONLY | os.O_NONBLOCK)
		humC=os.read(cfhumIO,1024)
		os.close(cfhumIO)
		cfwetIO=os.open(cfwet, os.O_RDONLY | os.O_NONBLOCK)
		wetC=os.read(cfwetIO,1024)
		os.close(cfwetIO)
		tempW=float(tempW)
		tempC=float(tempC)
		humW=float(humW)
		humC=float(humC)
		wetC=float(wetC)
		cwsuc=1
	except:
		cwsuc=0	
while True:
	try:
		wetIO=os.open(wetfilo, os.O_RDONLY | os.O_NONBLOCK)
		wet=os.read(wetIO,1024)
		os.close(wetIO)
		wet=float(wet)
		tempIO=os.open(tempfilo, os.O_RDONLY | os.O_NONBLOCK)
		humIO=os.open(humfilo, os.O_RDONLY | os.O_NONBLOCK)
		temp=os.read(tempIO,1024)
		hum=os.read(humIO,1024)
		os.close(tempIO)
		os.close(humIO)
		temp=float(temp)
		hum=float(hum)
		read=1
	except:
		read=0
		critical=1
	if temp<tempC and hum<humC and wet<wetC and read==1:
		critical=0
	if temp<tempW and hum<humW and read==1:
		warning=0
	if temp>=tempW:
		warning=1
	if hum>=humW:
		warning=1
	if temp>=tempC:
		critical=1
	if hum>=humC:
		critical=1
	if wet>=wetC:
		critical=1
	if critical==1 and silent==0:
		crit_ring=1
	if critical==0 and silent==0:
		crit_ring=0
	if crit_ring==1 and ring_act==0:
		ring=GPIO.PWM(7,4000)
		ring.start(50)
		ring_act=1
	if crit_ring==0:
		ring.stop()
		ring_act=0
	if ring_act==1 and silent==1:
		ring.stop()
		ring_act=0
	if warning==1 and critical==0 and blink_act==0:
		blink=GPIO.PWM(22,2)
		blink.start(1)
		blink_act=1
	if warning==0 and blink_act==1:
		blink.stop()
		blink_act=0
	if warning==1 and critical==1 and blink_act==1:
		blink.stop()
		blink_act=0
	if critical==1:
		GPIO.output(22,1)
	if critical==0:
		GPIO.output(22,0)
	
	if sc!=0:
		sc=sc-1
	if GPIO.input(16)==GPIO.HIGH:
		sc=120
		silent=1
	if sc==0 and silent==1:
		silent=0
	time.sleep(1)
