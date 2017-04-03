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

# custom modules - should be in file.
from modules.functions import *
from modules.graph_options import *
from modules.menus import *

# Use this to change the style of graph
plt.style.use('seaborn-notebook')


# =================== All the file handling ==========================

input("Choose .txt to use for data - press any key to continue")

# File location from user using pretty GUI
root = tk.Tk()                      # make it
root.withdraw()                     # how to
raw_path = filedialog.askopenfile() # what to
root.destroy()                      # get rid of

# This is needed to make the file path work correctly
file_path = raw_path.name

# Make sure the filename looks correct
print("\n")
print("File name is: {}".format(file_path.split('/')[-1]))


# Number of lines to scan for first non-commented line. Use to get the data
# start time and allow for comments at the beginning of files
lines_to_scan = 40
data_begin = data_start(file_path, lines_to_scan) # data_start is cutom function

# Imported function that runs through and get information from user. See modules
# file for more information
start_time = get_start(data_begin)

print("Start time is: {}".format(start_time))

# get_data is in moldules/functions.py file. This is what extracts the
# data given the input file
time, temperature, pressure, rel_hum = get_data(file_path, start_time)


# ========== Plotting Menu. Get user input for plotting ===============

# Could add options for different graph layouts. 
plot_options = [("Temperature", 1),
                ("Pressure", 2),
                ("Relative Humidity", 3),
                ("Plot all", 4),
                ("Plot and save all of the above", 5)]

user_selection = menu_maker(plot_options)

""" Calm down! Same thing repeated over and over
    save_place
    title
    plotting stuff
"""
if user_selection == 1:
    save_path = "{}_temperature.png".format(file_path.split('.')[0])
    title_string = 'Temperature for:' \
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, temperature, title_string, 'time', 'temperature(C)', save_path)


elif user_selection == 2:
    save_path = "{}_pressure.png".format(file_path.split('.')[0])
    title_string = 'pressure for:'\
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, pressure, title_string, 'time', 'pressure(hPa)', save_path)

elif user_selection == 3:
    save_path = "{}_RH.png".format(file_path.split('.')[0])
    title_string = 'RH for: {}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, rel_hum, title_string, 'time', 'Relavitve Humidity', save_path)

elif user_selection == 4:

    # With data, create save path and title to give the functions
    save_path = "{}_all.png".format(file_path.split('.')[0])
    title = 'All Data: {}'.format(file_path.split('.')[0].split('/')[-1])

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

elif user_selection == 5:

    # Temperature Plotting
    save_path = "{}_temperature.png".format(file_path.split('.')[0])
    title_string = 'Temperature for:' \
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, temperature, title_string, 'time', 'temperature(C)', save_path)

    # Pressure Plotting
    save_path = "{}_pressure.png".format(file_path.split('.')[0])
    title_string = 'pressure for:'\
        '{}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, pressure, title_string, 'time', 'pressure(hPa)', save_path)

    # Relative Humidity plotting
    save_path = "{}_RH.png".format(file_path.split('.')[0])
    title_string = 'RH for: {}'.format(file_path.split('.')[0].split('/')[-1])
    single_plot(time, rel_hum, title_string, 'time', 'Relavitve Humidity', save_path)


    # Plotting them all
    save_path = "{}_all.png".format(file_path.split('.')[0])
    title = 'All Data: {}'.format(file_path.split('.')[0].split('/')[-1])

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


