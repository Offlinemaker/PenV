import os
import sys
from optparse import OptionParser

tempfilo="/ramtmp/temp.penv"
humfilo="/ramtmp/hum.penv"
lightfilo="/ramtmp/light.penv"
wetfilo="/ramtmp/wet.penv"
doorfilo="/ramtmp/door.penv"

parser = OptionParser()

parser.add_option("-c","--temp","-1" , help="Temperature", action="store_true", dest="temp", default=False)
parser.add_option("-u","--hum","-2" , help="Humidity", action="store_true", dest="hum", default=False)
parser.add_option("-l","--light","-3" , help="Light", action="store_true", dest="light", default=False)
parser.add_option("-w","--wet","-4", help="Wetness", action="store_true", dest="wet", default=False)
parser.add_option("-d","--door","-5", help="Door", action="store_true", dest="door", default=False)
(options, args) = parser.parse_args()

if options.light==True:
	lightIO=os.open(lightfilo, os.O_RDONLY | os.O_NONBLOCK)
	light=os.read(lightIO,1024)
	sys.stdout.write(light)
	sys.stdout.write("\n")
	os.close(lightIO)
if options.wet==True:
	wetIO=os.open(wetfilo, os.O_RDONLY | os.O_NONBLOCK)
	wet=os.read(wetIO,1024)
	sys.stdout.write(wet)
        sys.stdout.write("\n")
	os.close(wetIO)
if options.temp==True:
	tempIO=os.open(tempfilo, os.O_RDONLY | os.O_NONBLOCK)
	temp=os.read(tempIO,1024)
	sys.stdout.write(temp)
        sys.stdout.write("\n")
	os.close(tempIO)
if options.hum==True:
	humIO=os.open(humfilo, os.O_RDONLY | os.O_NONBLOCK)
	hum=os.read(humIO,1024)
	sys.stdout.write(hum)
        sys.stdout.write("\n")
	os.close(humIO)
if options.door==True:
	doorIO=os.open(doorfilo, os.O_RDONLY | os.O_NONBLOCK)
	door=os.read(doorIO,1024)
	sys.stdout.write(door)
        sys.stdout.write("\n")
	os.close(doorIO)
