PenV
====

Pi Environmental Sensor

The PenV is meant to be adaptable and friendly in terms of API. The process to gather data saves it to a file in the RAM. With every new value this file gets overwritten. Every access to them is made non blockingly so multiple processes can simultaneously get a valid and up to date value.
There are three means of using that output at the moment, if you use all, any or none of the is up to you.
<dl>
  <dt>SNMP</dt>
  <dd>The most simple usage here. Basically it just echoes the value of the file.</dd>
  <dt>Alarm</dt>
  <dd>Very useful if you use the PenV to monitor some critical values, like air quality or humidity or temperature. It compares the Values from the files to the thresholds from /mon/vals and starts blinking and beeping (Blinkers and Beepers not included)</dd>
  <dt>LCD-Screen</dt>
  <dd>The most elaborate use in this programm so far. It uses a LCD that is connected to the UART. The values from the sensors get displayed on different screens that cycle (2 atm). When it detects a 'c' on RX it goes to mainenance mode, where the screen application stops and you can log in normally via serial connection. 
  (After you are done please use 'cleanexit.sh', otherwise the screen service wont start and you are locked out :( ) </dd>
</dl>
