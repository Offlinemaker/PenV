#!/bin/bash
#/etc/init.d/start_xalerts.sh

### BEGIN INIT INFO
# Provides: 		xstart_alerts.sh
# Required-Start:	$remote_fs $syslog
# Required-Stop:	$remote_fs $syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	PenV Alarm Service startup
# Description		Script to start the Alarm Service for the PenV
### END INIT INFO

case "$1" in
	start)
		echo "Starting PenV Alert Service"
		nohup sudo python /mon/alert_service.py &
		;;
	stop)
		echo "Stopping Pen VAlert Service"
		UNSV=($(ps aux | grep python | grep alert_service | grep sudo | cut -b11-14))
		kill $UNSV
		;;
	*)
		echo "Usage: /etc/init.d/start_alerts.sh {start|stop}"
		exit 1
		;;
esac

exit 0
