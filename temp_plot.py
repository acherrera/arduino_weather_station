"""
Created by Anthony Herrera to analyze Arduino weather station data.

This is just made to plot the temperature variable

"""

from modules.functions import get_start, get_data, data_start
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
from modules.graph_options import single_plot

the_file = 'datasets/testing_data/20170325_Response_Testing.TXT'

lines_to_scan = 40  # lines to scan for the first non-comment line

data_start = data_start(the_file, lines_to_scan)

start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

time, temperature, pressure, rel_hum = get_data(the_file, start_time)

if len(time) < 3:
    print("Please check starting times\nProgram Exiting")
    quit()

# With data, create save path and title to give the functions
save_path = "{}_temperature.png".format(the_file.split('.')[0])
title_string = 'Temperature for: {}'.format(the_file.split('.')[0].split('/')[2])

# This takes care of the plotting automatically
single_plot(time, temperature, title_string, 'time', 'temperature(C)',
        save_path)

