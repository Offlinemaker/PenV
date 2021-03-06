#!/bin/bash
#/etcn/init.d/start_screen.sh

### BEGIN INIT INFO
# Provides: 		start_screen.sh
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	LCD Screen Service startup
# Description		Script to start the (Pseudo)LCD Screen Service for the PenV
### END INIT INFO

case "$1" in
	start)
		echo "Starting LCD Screen Service"
		nohup sudo python /mon/screen.py &
		;;
	stop)
		echo "Stopping LCD Screen Service"
		UNSV=($(ps aux | grep python | grep screen.py | grep sudo | cut -b11-14))
		kill $UNSV
		;;
	*)
		echo "Usage: /etc/init.d/start_screen.sh {start|stop}"
		exit 1
		;;
esac

exit 0
