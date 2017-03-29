"""
Created by Anthony Herrera to analyze Arduino weather station data.

WHEN RUN: will need to hit enter in the command prompt area and/or set the desired starting time. Program
will wait until you tell it when you want it to start. Keep hitting enter to start at start time of data.

"""
# TODO put lines in graph where sensor was messed with, potentially skewing results
# TODO add temperature conversion availability. Need to update graph axis labels
# TODO add functionality for end time
# TODO make it an option to skip the 'start_time' option below


# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.


from modules.functions import get_start, get_data, data_start
from modules.graph_options import three_plots
from modules.menus import *

the_file = 'datasets/other_data/20170225_Car_Ride_Home.TXT'

lines_to_scan = 40  # lines to scan for the first non-comment line

data_start = data_start(the_file, lines_to_scan)

start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

time, temperature, pressure, rel_hum = get_data(the_file, start_time)

# this checks to make sure there is something to output
if len(time) < 3:
    print("Please check starting times\nProgram Exiting")
    quit()

# With data, create save path and title to give the functions
save_path = "{}.png".format(the_file.split('.')[0])
title = 'Sensor Data: {}'.format(the_file.split('.')[0].split('/')[2])

# This is the makes the three plots
three_plots(x=time,
            y1=temperature,
            y2=pressure,
            y3=rel_hum,
            title=title,
            xlabel='time',
            ylabel1='Temperature (C)',
            ylabel2='Pressure (hPa)',
            ylabel3='RH (%)',
            save_file=save_path)
