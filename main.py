"""
Created by Anthony Herrera to analyze Arduino weather station data.

WHEN RUN: will need to hit enter in the command prompt area and/or set the desired starting time. Program
will wait until you tell it when you want it to start. Keep hitting enter to start at start time of data.

"""

# TODO add temperature conversion availability. Need to update graph axis labels
# TODO add functionality for end time


# Time comes in form %04d%02d%02d_%02d%02d%02d - Because I made it that way.
# Data is of form: Time, Temperature, Pressure, Relative Humidity.

# Change this to False for day light savings time


#=====================Importing Modules============================

import tkinter as tk
from tkinter import filedialog
import numpy as np
import datetime


# custom modules - should be in file.
from modules.functions import *
from modules.graph_options import *
from modules.menus import *

# Use this to change the style of graph
plt.style.use('seaborn-notebook')

# ======================= DST correction ================

add_hour = True # False for minus one hour (winter)

if add_hour:
    time_correction = 1
else:
    time_correction = 0


# =================== All the file handling ==========================

input("Choose .txt to use for data - press 'enter' to continue")

file_path = GUI_file_selector()

# Make sure the filename looks correct
print("\n")
print("File name is: {}".format(file_path.split('/')[-1]))


# Number of lines to scan for first non-commented line. Use to get the data
# start time and allow for comments at the beginning of files
lines_to_scan = 40
data_begin = data_start(file_path, lines_to_scan) # data_start is cutom function

# Imported function that runs through and get information from user. See modules
# file for more information
# no DST corrrection because this is data start time. Not plotted
start_time = get_start(data_begin)

print("Start time is: {}".format(start_time))

# get_data is in moldules/functions.py file. This is what extracts the
# data given the input file

time, temperature, pressure, rel_hum = get_data(file_path, start_time)

# ===============Day Light Saving Time Correction ===================

for i in range(len(time)):
    time[i] = time[i] + datetime.timedelta(hours=time_correction)

# ========== Plotting Menu. Get user input for plotting ===============

# Could add options for different graph layouts. 
plot_options = [("Temperature", 1),
                ("Pressure", 2),
                ("Relative Humidity", 3),
                ("Plot all", 4),
                ("Plot and save all of the above", 5),
                ("ASOS Comparison", 6)]

user_selection = menu_maker(plot_options)

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

# ====================== ASOS Comparison Handling ============================

elif user_selection == 6:
    # ASOS handling
    input("\nNext Screen is the ASOS file input - press 'enter' to continue")

    official_file = GUI_file_selector()

    # appended "_ASOS" to data names to avoid potential conflicts
    station_ASOS, times_ASOS, temperature_ASOS, dew_point_ASOS, rel_hum_ASOS, dirct,\
    ASOS_mslp= parse_ASOS(official_file)

    station_ASOS = station_ASOS[0]

    print("\nASOS data loaded!\nWhat would you like to compare?")

    # Creating secondary menu for more user input
    ASOS_menu = [("Temperature", 1),
                 ("Pressure",2),
                 ("Relative Humidity",3),
                 ("Plot and save all of the above", 4)]


    ASOS_selection = menu_maker(ASOS_menu)


    # ================== Main area for ASOS data handling =======================



    # ================ Defining plotting functions ==========================
    """ 
    Because these are used twice, they are defined here for convience.
    Could be placed in moduls/graphing_options.py
    """
    def ASOS_temp_plot():
        # Temperature comparison - NOTE: ASOS data is in F
        x_plot, y_plot = pair_ASOS(times_ASOS, temperature_ASOS)
        y_plot = [((x-32)/1.8) for x in y_plot] #x is dummy variable. != x_plot

        # With data, create save path and title to give the functions
        save_path = "{}_temperature_comparison_{}.png"\
                .format(file_path.split('.')[0],
                station_ASOS)
        title = '{}: Temperature Comparison:' \
                '{}'.format(station_ASOS, file_path.split('.')[0].split('/')[-1])

        fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

        # Actually plotting the data - with labels and everything
        ax1 = plt.subplot(1, 1, 1)
        ax1.plot(x_plot, y_plot, label='Official Data')
        ax1.plot(time, temperature, label='unofficial data')

        # this is what make the x-axis format correctly
        xfmt = mdate.DateFormatter('%H:%M')
        ax1.xaxis.set_major_formatter(xfmt)
        fig.autofmt_xdate()

        plt.title(title)
        plt.ylabel('Temperature(C)')
        plt.xlabel('Time (Hour:Minutes)')

        plt.legend()
        plt.savefig(save_path)
        plt.show()

    def ASOS_press_plot():
        # Plotting function for pressure
        x_plot, y_plot = pair_ASOS(times_ASOS, ASOS_mslp)

        # With data, create save path and title to give the functions
        save_path = "{}_pressure_comparison_{}.png"\
                .format(file_path.split('.')[0],
                station_ASOS)
        title = '{}: Pressure Comparison:' \
                '{}'.format(station_ASOS, file_path.split('.')[0].split('/')[-1])


        fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

        # Actually plotting the data - with labels and everything
        ax1 = plt.subplot(1, 1, 1)
        ax1.plot(x_plot, y_plot, label='Official Data')
        ax1.plot(time, pressure, label='unofficial data')

        # this is what make the x-axis format correctly
        xfmt = mdate.DateFormatter('%H:%M')
        ax1.xaxis.set_major_formatter(xfmt)
        fig.autofmt_xdate()

        plt.title(title)
        plt.ylabel('Pressure (hPa)')
        plt.xlabel('Time (Hour:Minutes)')

        plt.legend()
        plt.savefig(save_path)
        plt.show()

    def ASOS_humidity_plot():
        # Plotting function for humidity
                x_plot, y_plot = pair_ASOS(times_ASOS, rel_hum_ASOS)

                # With data, create save path and title to give the functions
                save_path = "{}_humidity_comparison_{}.png"\
                        .format(file_path.split('.')[0],
                        station_ASOS)
                title = '{}: humidity Comparison:' \
                        '{}'.format(station_ASOS,
                                file_path.split('.')[0].split('/')[-1])

                fig = plt.figure()  # This is the 'canvas' of the plot. Used later for changes

                # Actually plotting the data - with labels and everything
                ax1 = plt.subplot(1, 1, 1)
                ax1.plot(x_plot, y_plot, label='Official Data')
                ax1.plot(time, rel_hum, label='Unofficial data')

                # this is what make the x-axis format correctly
                xfmt = mdate.DateFormatter('%H:%M')
                ax1.xaxis.set_major_formatter(xfmt)
                fig.autofmt_xdate()

                plt.title(title)
                plt.ylabel('Relative Humidity (%)')
                plt.xlabel('Time (Hour:Minutes)')

                plt.legend()
                plt.savefig(save_path)
                plt.show()





    if ASOS_selection == 1:
        # Temperature plotting
        ASOS_temp_plot()

    if ASOS_selection == 2:
        # Pressure comparison: ASOS is sea level pressure
        ASOS_press_plot()


    if ASOS_selection == 3:
        # Relative Humidity comparison
        ASOS_humidity_plot()

    if ASOS_selection == 4:
        # All of the above

        ASOS_temp_plot()
        ASOS_press_plot()
        ASOS_humidity_plot()
