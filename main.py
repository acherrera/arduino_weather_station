"""
Created by Anthony Herrera to analyze Arduino weather station data.

WHEN RUN: will need to hit enter in the command prompt area and/or set the desired starting time. Program
will wait until you tell it when you want it to start. Keep hitting enter to start at start time of data.

"""

# TODO add temperature conversion availability. Need to update graph axis labels
# TODO add functionality for end time


# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.


#===================== Importing Modules============================

import tkinter as tk
from tkinter import filedialog
from modules.functions import *
from modules.graph_options import *
from modules.menus import *

plt.style.use('seaborn-notebook')


# =================== All the file handling ==========================

# File location


the_file ="/home/tony/Centered/weather_station" \
        "/datasets/testing_data/Response2/20170329_Response_Test.TXT"

print("\n")
print("File name is: {}".format(the_file.split('/')[-1]))

""" This is for VIM file finding. Ignore if not using VIM
/home/tony/Centered/weather_station/datasets/testing_data/Response4/20170330_Response_test.txt
"""

# Number of lines to scan for first non-commented line. Use to get the data
# start time and allow for comments at the beginning of files
lines_to_scan = 40
data_start = data_start(the_file, lines_to_scan)

# Import function that runs through and get information from user. See modules
# file for more information
start_time = get_start(data_start)

print("Start time is: {}".format(start_time))

# get_data is in moldules/functions.py file. This is what extracts the
# data given the input file
time, temperature, pressure, rel_hum = get_data(the_file, start_time)

# this checks to make sure there is something to output
if len(time) < 3:
    print("Please check starting times\nProgram Exiting")
    quit()



# ========== Plotting Menu. Get user input for plotting ===============

# Could add options for different graph layouts. 
plot_options = [("Temperature", 1),
                ("Pressure", 2),
                ("Relative Humidity", 3),
                ("Plot all", 4)]

user_selection = menu_maker(plot_options)

""" Calm down! Same thing repeated over and over
    save_place
    title
    plotting stuff
"""
if user_selection == 1:
    save_path = "{}_temperature.png".format(the_file.split('.')[0])
    title_string = 'Temperature for:' \
        '{}'.format(the_file.split('.')[0].split('/')[-1])
    single_plot(time, temperature, title_string, 'time', 'temperature(C)', save_path)


elif user_selection == 2:
    save_path = "{}_pressure.png".format(the_file.split('.')[0])
    title_string = 'pressure for:'\
        '{}'.format(the_file.split('.')[0].split('/')[-1])
    single_plot(time, pressure, title_string, 'time', 'pressure(hPa)', save_path)

elif user_selection == 3:
    save_path = "{}_RH.png".format(the_file.split('.')[0])
    title_string = 'RH for: {}'.format(the_file.split('.')[0].split('/')[-1])
    single_plot(time, rel_hum, title_string, 'time', 'Relavitve Humidity', save_path)

elif user_selection == 4:

    # With data, create save path and title to give the functions
    save_path = "{}_all.png".format(the_file.split('.')[0])
    title = 'All Data: {}'.format(the_file.split('.')[0].split('/')[-1])

    # This monster makes the three plots
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
