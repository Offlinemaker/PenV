SHELL := /bin/bash
all:
echo "Muffin to do here!"
install:

FIND="#PenV_Setup Complete here"
VGL=$(egrep "$FIND" /etc/fstab)



echo "Setting up Temporary FS"
if [[ "$FIND" != "$VGL" ]]; then

		#Temp FS einbinden
		sudo echo "tmpfs	/ramtmp	tmpfs defaults,size=60M 0 0" >> /etc/fstab
		sudo echo "#PenV_Setup Complete here" >> /etc/fstab
		echo "Temporary FS created"
	else
		echo "TempFS already created"
	fi



VGL=$(egrep "$FIND" /etc/sudoers)
echo "Modding Sudoers File"
if [[ "$FIND" != "$VGL" ]]; then
		#Sudoers: zuerst Alias für python einbauen
		sudo echo "Cmnd_Alias DOPY = /usr/bin/python" >> /etc/sudoers
		#Und jetzt monuser auch
		sudo echo "User_Alias MONUSER = snmp, python" >> /etc/sudoers
		#Berechtigungen
		sudo echo "MONUSER ALL=(ALL) NOPASSWD: DOPY" >> /etc/sudoers
		sudo echo "#PenV_Setup Complete here" >> /etc/sudoers
		echo "Sudoers file modded"
	else
		echo "Sudoers file already modded"
	fi




VGL=$(egrep "$FIND" /etc/snmp/snmpd.conf)
echo "Configuring SNMP-Daemon"
if [[ "$FIND" != "$VGL" ]]; then
		#In snmpd.conf
		sudo echo "rocommunity getmon 10.0.0.0/8" >> /etc/snmp/snmpd.conf
		sudo echo "extend .1.3.6.1.4.1.27654.3.1 get_temp /mon/get_temp.sh
		extend .1.3.6.1.4.1.27654.3.2 get_hum /mon/get_hum.sh
		extend .1.3.6.1.4.1.27654.3.3 get_light /mon/get_light.sh
		extend .1.3.6.1.4.1.27654.3.4 get_wet /mon/get_wet.sh
		extend .1.3.6.1.4.1.27654.3.5 get_wet /mon/get_door.sh" >> /etc/snmp/snmpd.conf
		sudo echo "#PenV_Setup Complete here" >> /etc/snmp/snmpd.conf
		echo "SNMP-Daemon Configuration Complete"
	else
		echo "SNMP-Daemon already Configured"
	fi




FIND="#blacklist i2c-bcm2708"
VGL=$(egrep "$FIND" /etc/modprobe.d/raspi-blacklist.conf)
echo "Activating I2C-Bus"
if [[ "$FIND" != "$VGL" ]]; then
		sed -i 's/blacklist i2c-bcm2708/#blacklist i2c-bcm2708/g' /etc/modprobe.d/raspi-blacklist.conf
		echo "I2C now Activated"
	else
		echo "I2C has already been Activated"
	fi



FIND="#T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100"
VGL=$(egrep "$FIND" /etc/inittab)
echo "Deactivating default Serial Session (I need it for the LCD-Screen)"
if [[ "$FIND" != "$VGL" ]]; then
		sed -i 's/T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100/#T0:23:respawn:/sbin/getty -L ttyAMA0 115200 vt100/g' /etc/inittab
		echo "Serial Session now Deactivated"
	else
		echo "Serial Session has already been Deactivated"
	fi


#Mon - Files nach /mon/ kopieren
sudo mkdir /mon/
sudo mkdir /mon/vals
sudo cp ./mon/* /mon/
sudo cp ./mon/vals/* /mon/vals

#bootup-Scripte kopieren
sudo cp ./boot/* /etc/init.d/
sudo chmod +x /etc/init.d/penv_*
sudo update-rc.d penv_getservice.sh start
sudo update-rc.d penv_screenservice.sh start
sudo update-rc.d penv_xalertservice.sh start

#cleanexit script nach /usr/local/bin kopieren
sudo cp ./bin/* /usr/local/bin
sudo chmod a+x /usr/local/bin/cleanexit.sh

echo "Everything is done now. You should restart the Pi now and connect the hardware while it is of"
echo "Good luck!"
