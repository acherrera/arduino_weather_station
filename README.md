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

Working on limiting the scope of the project. Example: do not need to have
every possible option included to make this work. 

### Make file to plot single varible

This should be easy - make a temperature only graph
                    - make a pressure only graph
                    - make a humidity only graph

# Other Interesting Links
Home made sonic anemometer: https://soldernerd.com/arduino-ultrasonic-anemometer/
