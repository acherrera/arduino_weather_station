# Arduino Weather Station
Contains files pertaining to the building of a home made weather station. Will be used for a 
school project comparing homemade to professional grade measurements.

# Project Outline
The project can be broken down into two three separate sections. These is the ATMega (Arduino) programming,
the hardware and wiring, and the processing of data. The Arduino programming is done in C; technically a modified C
for Arduino. The data is processed in Python language. 

# Project Notes

## Physical Build issues
The current designs seems to store a lot of heat in the system, making it much slower to
respond than the BME280 on its own. Need to create remote sensor to reduce the heat absorbed 
by the sensor from the rest of the sensing equipments. This is a small error, but will skew 
the data from expected. "Bathroom_fan_pressure_test" is a good example as the station had 
be brought inside minutes before the fan pressure test and it had yet to reach steady state. 

Additionally, the heating of the surroundings and radiation into the box are causing significant 
fluctuations and bizarre behaviour.  

Will attempt to fix this by mounting the sensor on a small standoff above 
or to the side of the board. Will test before and after for results

## Things to do
### Make Single Program with Options
Make a single program to process all different standard types of data. 
May need to break up program in modules for more clear operation. 

Options to graph include: 
* choose variables to graph
* choose to save graph
* enter variable name (temperature, pressure, humidity)
* choose start and end times

### Issue Relating to the Code Base
Working to modularize the program to make the main program easier to understand 
and aid in fixing issues later. 
 
The graphing methods will be broken down into several separate section for ease
of calling later. This will allow the options to be shortened down to one single line 
of code and call

### Use Python to Live Plot Data
The Arduino has the ability to send data out and the computer can take this data 
and live plot it. This would be useful in simple experiments with the systems such as temperature response

### Test Alternative Arduino Sketches
There are a few other Arduino sketches that can be built and tested for usability. 

These are:
* Max speed read - no delays and use millis() instead of the building date and time

* Live Plotting Mode: Output the variables so a Python program and live plot the variables being measured. 

# Version 2.0
The next step is miniaturizing and making more permanent. Current set up is large and relatively
expensive. 

# Other Interesting Links
Home made sonic anemometer: https://soldernerd.com/arduino-ultrasonic-anemometer/
