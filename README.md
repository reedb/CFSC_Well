# CFSC_Well
Collins Farm Well

The well is 105' deep and the majority of the water comes in at 85'. 
The static water level in the well is at 15'. 

The Well Bore Water Level Sensor is just above the well pump at 80 feet.
When it reads close to zero, the pump should not be run (out of water).

Historical Well Bore Water Level Data (Well@Off): <br />
08-19-2015 : 37'    <br />
08-23-2015 : 35'    <br />
08-24-2015 : 33'    <br />
01-25-2016 : 64'    <br />
05-08-2016 : 45'    <br />
07-12-2017 : 25.5'  <br />
07-21-2017 : 31.7'  <br />
09-17-2017 : 24.14' <br />
10-24-2017 : 29.42' <br />
02-06-2018 : 37.5'  <br />
08-21-2018 : 23.43' <br />
05-05-2019 : 36.12' <br />
05-24-2019 : 35.06' <br />
05-26-2019 : 35.06' <br />

Overview well control:
![alt text](https://github.com/reedb/CFSC_Well/blob/master/control_overview.jpg)

Closeup of well control display when showing level at "Well@Off":
![alt text](https://github.com/reedb/CFSC_Well/blob/master/control_display_welloff.jpg)

## Pump Control Details (pump_control.ino)
START_HEIGHT_PERCENT 90     // Pump starts when tank level drops to this value <br />
STOP_HEIGHT_PERCENT  100    // Pump stops when tank level rises to this value <br />
ALARM_HEIGHT_PERCENT 80     // Pump stops alarm sounds when tank level drops to this value <br />
