# CFSC_Well
Collins Farm Well

The well is 105' deep and the majority of the water comes in at 85'. 
The static water level in the well is at 15'. 

The Well Bore Water Level Sensor is just above the well pump at 80 feet.
When it reads close to zero, the pump should not be run (out of water).

Historical Well Bore Water Level Data (Well@Off) all data points: <br />
![alt text](https://github.com/reedb/CFSC_Well/blob/master/time_series.png?raw=true)

Historical Well Bore Water Level Data (Well@Off) one year cycle: <br />
![alt text](https://github.com/reedb/CFSC_Well/blob/master/year_cycle.png?raw=true)

Overview well control:
![alt text](https://github.com/reedb/CFSC_Well/blob/master/control_overview.jpg)

Closeup of well control display when showing level at "Well@Off":
![alt text](https://github.com/reedb/CFSC_Well/blob/master/control_display_welloff.jpg)

## Pump Control Details (pump_control.ino)
START_HEIGHT_PERCENT 90     // Pump starts when tank level drops to this value <br />
STOP_HEIGHT_PERCENT  100    // Pump stops when tank level rises to this value <br />
ALARM_HEIGHT_PERCENT 80     // Pump stops alarm sounds when tank level drops to this value <br />
