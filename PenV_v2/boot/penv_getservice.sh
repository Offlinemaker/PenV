#!/bin/bash
#/etc/init.d/start_get.sh

### BEGIN INIT INFO
# Provides: 		start_get.sh
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	PenV Data Service startup
# Description		Script to start the (Pseudo)Data Service for the PenV
### END INIT INFO

case "$1" in
	start)
		echo "Starting PenV Data Service"
		nohup sudo python /mon/fget_data.py &
		;;
	stop)
		echo "Stopping PenV Data Service"
		UNSV=($(ps aux | grep python | grep fget | grep sudo | cut -b11-14))
		kill $UNSV
		;;
	*)
		echo "Usage: /etc/init.d/start_get.sh {start|stop}"
		exit 1
		;;
esac

exit 0
